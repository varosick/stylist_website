from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from tempus_dominus.widgets import DateTimePicker

from users.models import Review, ScheduleDate, User, UserServices
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    """
    Logging form inherited from the off-the-shelf Django AuthenticationForm
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'name': "username",
        'id': "modal-authorization__input-mail",
        'placeholder': "Введите имя пользователя",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password",
        'name': "Пароль",
        'id': "modal-authorization__input-phone",
        'placeholder': "Введите пароль",
    }))

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(UserCreationForm):
    """
    Registration form inherited from the off-the-shelf Django UserCreationForm
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "first_name",
            'id': "modal-registration__input-name",
            'placeholder': "Имя"
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "last_name",
            'id': "modal-registration__input-surname",
            'placeholder': "Фамилия"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'type': "email",
            'name': "email",
            'id': "modal-registration__input-email",
            'placeholder': "E-mail"
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "username",
            'id': "modal-registration__input-username",
            'placeholder': "Введите имя пользователя, как в Instagram"
        })
    )

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'type': "date",
        'name': "date_of_birth",
        'id': "modal-registration__input-date-of-birth",
        'placeholder': "Введите дату рождение"
    }))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': "password",
            'name': "password1",
            'id': "modal-registration__input-password1",
            'placeholder': "Введите пароль",
            'autocomplete': 'new-password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': "password",
            'name': "password2",
            'id': "modal-registration__input-password2",
            'placeholder': "Повторите пароль",
            'autocomplete': 'new-password'
        })
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)

        # Delayed sending of an email to confirm registration with Celery
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(forms.ModelForm):
    """
    Form for displaying user data in the profile
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "first_name",
            'id': "lk-my-profil-content-data__input-first-name",
            'placeholder': "Имя"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "last_name",
            'id': "lk-my-profil-content-data__input-last-name",
            'placeholder': "Фамилия"
        })
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': "date",
            'name': "date_of_birth",
            'id': "lk-my-profil-content-data__input-date-of-birth",
            'placeholder': "Дата рождения"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'type': "email",
            'name': "email",
            'id': "lk-my-profil-content-data__input-email",
            'placeholder': "Электронная почта"
        })
    )
    tg_link = forms.URLField(
        widget=forms.URLInput(attrs={
            'type': "url",
            'name': "tg_link",
            'id': "lk-my-profil-content-data__input-tg-link",
            'placeholder': "Ссылка на Telegram"
        }),
        required=False
    )
    inst_link = forms.URLField(
        widget=forms.URLInput(attrs={
            'type': "url",
            'name': "inst_link",
            'id': "lk-my-profil-content-data__input-inst-link",
            'placeholder': "Ссылка на Instagram"
        }),
        required=False
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'type': "file",
            'name': "image",
            'id': "lk-my-profil-content-data__input-image",
            'placeholder': "Изображение",
            'onchange': "previewImage(event)",
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'email', 'tg_link', 'inst_link', 'image')


class ServicePurchaseForm(forms.ModelForm):
    """
    Service purchase form with tempus_dominus connection to display a custom calendar
    """
    datetime_of_service = forms.DateTimeField(widget=DateTimePicker(options={
        'format': 'YYYY-MM-DD HH:mm',
        'useCurrent': False,
        'stepping': 60,
        'enabledHours': [10, 11, 12, 13, 14, 15, 16, 17, 18],
        'icons': {
            'time': "fa fa-clock-o",
            'date': "fa fa-calendar",
            'up': "fa fa-arrow-up",
            'down': "fa fa-arrow-down"
        },
    },
        attrs={
            'placeholder': 'Выберете дату и время услуги'}
    ))
    class Meta:
        model = UserServices
        fields = ('datetime_of_service', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Updates available dates before loading the form
        self.fields['datetime_of_service'].widget.js_options['enabledDates'] = list(map(lambda x: x.strftime("%Y-%m-%d"), ScheduleDate.objects.filter(is_booked=False).values_list('date', flat=True)))



class ReviewAddForm(forms.ModelForm):
    """
    Form for adding user review
    """
    review = forms.CharField(widget=forms.Textarea(attrs={
        'style': 'width: 100%; resize: none;',
        'rows': 10,
    }))
    class Meta:
        model = Review
        fields = ('review', )


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Password change form inherited from PasswordChangeForm
    """
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Новый пароль',
            'class': 'lk-my-profil-content-data__input',
        }),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение нового пароля',
            'class': 'lk-my-profil-content-data__input',
        }),
    )
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Старый пароль',
            'class': 'lk-my-profil-content-data__input',
        }),
    )

class UserForgotPasswordForm(PasswordResetForm):
    """
    Form for sending an e-mail about password change
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'type': "email",
            'name': "email",
            'id': "modal-recovery__input",
            'placeholder': "Введите Email"
        })
    )

class UserSetNewPasswordForm(SetPasswordForm):
    """
    Form for changing user password after confirmation
    """
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Новый пароль',
            'class': 'modal-recovery__input',
        }),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение нового пароля',
            'class': 'modal-recovery__input',
            'type': "password",
        }),
    )

