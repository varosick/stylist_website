from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
import uuid
from users.models import User, EmailVerification, UserGuides, UserServices


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    email_verification = EmailVerification.objects.create(user=user, expiration=expiration, code=uuid.uuid4())
    email_verification.send_verification_email()

@shared_task
def send_emails_guides(user_guide_id):
    user_guide = UserGuides.objects.get(id=user_guide_id)
    user_guide.send_email_to_stylist()
    user_guide.send_email_to_user()

@shared_task
def send_emails_services(user_service_id):
    user_service = UserServices.objects.get(id=user_service_id)
    user_service.send_email_to_stylist()
    user_service.send_email_to_user()