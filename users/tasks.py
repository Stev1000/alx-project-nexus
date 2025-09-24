from celery import shared_task

@shared_task
def send_welcome_email(username):
    print(f"Sending welcome email to {username}")
    return f"Email sent to {username}"
