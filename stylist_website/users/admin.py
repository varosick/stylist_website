from django.contrib import admin
from users.models import User, Review, UserServices, ScheduleDate, EmailVerification, UserGuides


# Register your models here.
@admin.register(User)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Review)
class Admin(admin.ModelAdmin):
    pass

@admin.register(UserServices)
class Admin(admin.ModelAdmin):
    pass

@admin.register(ScheduleDate)
class Admin(admin.ModelAdmin):
    pass

@admin.register(EmailVerification)
class Admin(admin.ModelAdmin):
    pass

@admin.register(UserGuides)
class Admin(admin.ModelAdmin):
    pass