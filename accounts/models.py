from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .constants import ROLES_CHOICES


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


# We can also make a separate model class for Roles so that we can add more Roles in the future.
class User(AbstractUser, TimeStampedModel):
    mobile = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    role = models.CharField(choices=ROLES_CHOICES, max_length=1024, blank=True, null=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        """Returns the username of the User when it is printed in the console"""
        return self.username


class Team(TimeStampedModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    team_leader = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_team_lead", blank=True, null=True,
                                    on_delete=models.PROTECT)
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='team_member_user')
