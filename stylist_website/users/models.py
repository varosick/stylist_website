from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse

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
        """
        Overrides the save method to send email to the user after a change in payment status
        """
        if self.pk:
            old_instance = UserServices.objects.get(pk=self.pk)
            old_payment_status = old_instance.payment_status
        else:
            old_payment_status = None

        super().save(*args, **kwargs)

        # f payment_status has changed, execute the logic of sending email
        if old_payment_status is not None and old_payment_status != self.payment_status:
            self.send_payment_status_email()

    def send_payment_status_email(self):
        """
        Sending an email to a user when the payment status changes
        """
        subject = f'Подтверждение внесение предоплаты услуги {self.service.name} {self.service.category.name}'
        message = f'''Привет, {self.user.first_name}, это Ваш персональный стилист Маша! 

Спасибо Вам за внесение предоплаты! Оплата прошла успешно и теперь дата зарезервирована за Вами! 

Скоро я пришлю всю информацию по подготовке к услуге Вам в Директ в Инстаграм, так что не забываете проверять сообщения 

Если будут вопросы, не стесняйтесь, пишите мне в Директ Инстаграм @kallishevich или в Телеграмм @kallishevich'''
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
        """
        Sending an e-mail to the user after successful purchase of the service
        """
        subject = f'Спасибо за покупку услуги {self.service.name} {self.service.category.name}'
        message = f'''Привет, {self.user.first_name}, это я Маша. Спасибо Вам за резервацию и внесение предоплаты! 

В течение 48 часов я проверю вашу оплату

После этого, я пришлю Вам всю информацию о подготовке к услуге в Директ Инстаграмм, так что не забывайте проверять сообщения! 

Я также напомню Вам за день до назначенной даты о нашей предстоящей встрече!

Если будут вопросы, не стесняйтесь, пишите мне в Директ Инстаграм @kallishevich или в Телеграмм @kallishevich

Спасибо Вам за доверие!'''
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def send_email_to_stylist(self):
        """
        Sending an e-mail to the stylist after successful purchase of the service
        """
        subject = f'Покупка услуги {self.service.name} {self.service.category.name}'
        message = f'''{self.user.first_name} {self.user.last_name} ({self.user.username}) приобрел услугу {self.service.name} {self.service.category.name}. 
        Нужно проверить предоплату по ссылке, вся подробная информация там же: {settings.DOMAIN_NAME}/admin/users/userservices/{self.id}/change . Ссылки для связи inst: {self.user.inst_link}, tg: {self.user.tg_link}
        '''
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
        """
        Overrides the save method to send email to the user after a change in payment status
        """
        if self.pk:
            old_instance = UserGuides.objects.get(pk=self.pk)
            old_payment_status = old_instance.payment_status
        else:
            old_payment_status = None

        # Вызов стандартного метода save
        super().save(*args, **kwargs)

        # If payment_status has changed, execute the logic of sending email
        if old_payment_status is not None and old_payment_status != self.payment_status:
            self.send_payment_status_email()

    def send_payment_status_email(self):
        """
        Sending an email to a user when the payment status changes
        """
        subject = f'Подтверждение оплаты гайда {self.guide.name}'
        message = f'''Привет, {self.user.first_name}, это Ваш персональный стилист Маша! 
Спасибо Вам за покупку моего гайда! Оплата прошла успешно и теперь он доступен в вашем личном кабинете в разделе «Мои гайды»

Если будут вопросы, не стесняйтесь, пишите мне в Директ Инстаграм @kallishevich или в Телеграмм @kallishevich'''
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
        """
        Sending an e-mail to the user after successful purchase of the guide
        """
        subject = f'Спасибо за покупку гайда {self.guide.name}'
        message = f'''Привет, {self.user.first_name}, это я Маша. 
Спасибо Вам за доверие и покупку моего гайда! Я очень старалась сделать его максимально полноценным и полезным для Вас! 
        
После проверки вашей оплаты он станет доступным в Вашем личном кабинете в разделе «мои гайды»
Проверка занимает до 48 часов

Если будут вопросы, не стесняйтесь, пишите мне в Директ Инстаграм @kallishevich или в Телеграмм @kallishevich'''
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def send_email_to_stylist(self):
        """
        Sending an e-mail to the stylist after successful purchase of the guide
        """
        subject = f'Покупка гайда {self.guide.name}'
        message = f'''{self.user.first_name} {self.user.last_name} ({self.user.username}) приобрел гайд. 
Нужно проверить оплату и подтвердить по ссылке: {settings.DOMAIN_NAME}/admin/users/userguides/{self.id}/change/
Ссылки для связи inst: {self.user.inst_link}, tg: {self.user.tg_link}'''
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

    def __str__(self):
        return f'Email verification for {self.user.email}'

    def send_verification_email(self):
        """
        Sending an e-mail to the user to confirm the mail
        """
        link = reverse('users:email_verify', kwargs={'email': self.user.email, 'code': self.code})
        verify_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение адреса электронной почты для пользователя {self.user.username}'
        message = (f'''Привет, {self.user.first_name}, это Ваш персональный стилист Маша! 
        
Спасибо Вам за регистрацию, она прошла успешна! Для подтверждения электронной почты переходи по ссылке: {verify_link}
        
Теперь у Вас есть свой личный профиль, где Вы найдете все приобретенные Вами услуги и гайды, которые я подготовлю для Вас.
Если будут вопросы, не стесняйтесь, пишите мне в Директ инстаграм @kallishevich или в телеграмм @kallishevich. 
        
Мне не терпится начать нашу работу!. ''')
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

