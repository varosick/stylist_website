from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from products.models import Guide, Product


class User(AbstractUser):
    image = models.ImageField(upload_to="media/users/users_images/", null=True, blank=True)
    inst_link = models.URLField(null=True, blank=True)
    tg_link = models.URLField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

class ScheduleDate(models.Model):
    date = models.DateField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date.strftime("%d-%m %A %H:%M")}'

class UserServices(models.Model):
    class Payment(models.IntegerChoices):
        NOT_PAID = 0
        PREPAYMENT = 1
        PAID = 2

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    payment_status = models.IntegerField(default=0, choices=Payment)
    datetime_of_service = models.DateTimeField(default=datetime.now)
    gdrive_file_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = UserServices.objects.get(pk=self.pk)
            old_payment_status = old_instance.payment_status
        else:
            old_payment_status = None

        # Вызов стандартного метода save
        super().save(*args, **kwargs)

        # Если payment_status изменился, выполняем логику отправки email
        if old_payment_status is not None and old_payment_status != self.payment_status:
            self.send_payment_status_email()

    def send_payment_status_email(self):
        # Логика отправки email
        subject = 'Изменение статуса оплаты'
        message = f'Статус оплаты вашей услуги "{self.service}" изменен на {self.get_payment_status_display()}.'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def __str__(self):
        return f'{self.user.username} {self.service}'

    def send_email_to_user(self):
        subject = f'Спасибо за покупку услуги {self.service.name} {self.service.category.name}'
        message = f'Привет, {self.user.first_name}, это я Маша. Спасибо за покупку услуги! После проверки оплаты тебе придет мейл и услуга будет доступна в личном кабинете'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def send_email_to_stylist(self):
        subject = f'Покупка услуги {self.service.name} {self.service.category.name}'
        message = f'{self.user.first_name} {self.user.last_name} приобрел услугу. Нужно проверить оплату'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sokolovamariia55@gmail.com'],
            fail_silently=False,
        )


class UserGuides(models.Model):
    class Payment(models.IntegerChoices):
        NOT_PAID = 0
        PAID = 1

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    payment_status = models.IntegerField(default=0, choices=Payment)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = UserGuides.objects.get(pk=self.pk)
            old_payment_status = old_instance.payment_status
        else:
            old_payment_status = None

        # Вызов стандартного метода save
        super().save(*args, **kwargs)

        # Если payment_status изменился, выполняем логику отправки email
        if old_payment_status is not None and old_payment_status != self.payment_status:
            self.send_payment_status_email()

    def send_payment_status_email(self):
        subject = 'Изменение статуса оплаты'
        message = f'Статус оплаты вашей услуги "{self.guide}" изменен на {self.get_payment_status_display()}.'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def __str__(self):
        return f'{self.user.username} {self.guide}'

    def send_email_to_user(self):
        subject = f'Спасибо за покупку гайда {self.guide.name}'
        message = f'Привет, {self.user.first_name}, это я Маша. Спасибо за покупку гайда! После проверки оплаты тебе прийдет мейл и гайд будет доступен в личном кабинете'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def send_email_to_stylist(self):
        subject = f'Покупка гайда {self.guide.name} '
        message = f'{self.user.first_name} {self.user.last_name} приобрел гайд. Нужно проверить оплату'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['sokolovamariia55@gmail.com'],
            fail_silently=False,
        )


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Email verification for {self.user.email}'


    def send_verification_email(self):
        link = reverse('users:email_verify', kwargs={'email': self.user.email, 'code': self.code})
        verify_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение адреса электронной почты для пользователя {self.user.username}'
        message = (f'''Привет, {self.user.first_name}, это Ваш персональный стилист Маша! Спасибо Вам за регистрацию, она прошла успешна! Для подтверждения электронной почты переходи по ссылке: {verify_link} 
        Теперь у Вас есть свой личный профиль, где Вы найдете все купленные Вами услуги и гайды, а также все файлы, которые я подготовлю для Вас
        Если будут вопросы, не стесняйтесь, пишите мне в Директ инстаграм (@kallishevich) или в телеграмм (@kallishevich) ) Мне не терпится начать нашу работу!. ''')
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

