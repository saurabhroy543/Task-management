from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from accounts.models import User, Team


@shared_task(bind=True)
def email_for_new_task(extra=None, name=None, team=None):
    if team:
        from_email = settings.DEFAULT_EMAIL_FROM
        team_data = Team.objects.filter(id=team).first()
        to = team_data.team_leader.email
        subject = 'New Task'
        message = 'A new task is created for you team : \n name: {0} \n name of team: {1}'.format(name, team_data.name)
        print(to, message)
        msg = EmailMultiAlternatives(subject, message, from_email, [to])
        msg.send()
    return None
