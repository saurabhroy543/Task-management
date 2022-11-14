from django.db import models
from accounts.models import TimeStampedModel, Team
from task.constants import STATUS_CHOICES
from django.conf import settings


class Task(TimeStampedModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    team = models.ForeignKey(Team, related_name="team_assigned", blank=True, null=True,
                             on_delete=models.PROTECT)
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='team_members_task')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1024, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

