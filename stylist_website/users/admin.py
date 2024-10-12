from django.contrib import admin

from users.models import (EmailVerification, Review, ScheduleDate, User,
                          UserGuides, UserServices)


# Register your models here.
@admin.register(User)
class Admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_verified_email')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login', 'password')


@admin.register(Review)
class Admin(admin.ModelAdmin):
    list_display = ('user', 'date', 'is_approved')
    list_editable = ('is_approved',)
    readonly_fields = ('user', 'date', )
    search_fields = ('user__username', 'user__email')
    ordering = ('is_approved',)
    actions = ('set_approved',)
    list_filter = ('is_approved',)

    @admin.action(description='Опубликовать выбранные отзывы')
    def set_approved(self, request, queryset):
        count = queryset.update(is_approved=True)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(UserServices)
class Admin(admin.ModelAdmin):
    list_display = ('service', 'user__username', 'payment_status')
    search_fields = ('user__username', 'user__email', 'service__name')
    readonly_fields = ('user', 'service',)
    list_editable = ('payment_status',)
    list_filter = ('payment_status', 'service')


@admin.register(ScheduleDate)
class Admin(admin.ModelAdmin):
    list_display = ('date', 'is_booked')
    ordering = ('date',)
    search_fields = ('date',)
    list_editable = ('is_booked',)
    actions = ('set_booked', )

    @admin.action(description='Установить бронь на выбранные даты')
    def set_booked(self, request, queryset):
        count = queryset.update(is_booked=True)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(EmailVerification)
class Admin(admin.ModelAdmin):
    list_display = ('user__email', 'user__username', 'code')
    readonly_fields = ('user', 'code')
    search_fields = ('user__email', 'user__username', )


@admin.register(UserGuides)
class Admin(admin.ModelAdmin):
    list_display = ('guide', 'user__username', 'payment_status')
    search_fields = ('user__username', 'user__email', 'guide__name')
    readonly_fields = ('user', 'guide', )
    list_editable = ('payment_status', )
    actions = ('set_paid', )
    list_filter = ('payment_status', 'guide')

    @admin.action(description='Подтвердить оплату у выбранных пользователей')
    def set_paid(self, request, queryset):
        count = queryset.update(payment_status=UserGuides.Payment.PAID)
        self.message_user(request, f'Изменено {count} записей')