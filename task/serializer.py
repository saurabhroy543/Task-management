from rest_framework import serializers
from .celery_task import email_for_new_task
from accounts.serializer import TeamSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    team_data = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', None)
        team = data.get('team', None)
        user = self.context['request'].user
        if self.context['request'].user.role == 'MEMBER':
            if user not in self.instance.team_members.all():
                raise serializers.ValidationError(
                    {'detail': 'You cannot update this task,You are not assigned to this task'})
            fields = ['name', 'team', "team_members", 'started_at', 'completed_at']
            for field in fields:
                if field in self.context['request'].data:
                    raise serializers.ValidationError({'detail': 'You are allowed to edit status only'})
        else:
            if not name or not team:
                raise serializers.ValidationError({'detail': 'Name and team must be given'})
            if self.context['request'].user.role == 'ADMIN':
                email_for_new_task.s(name=name, team=team.id).apply_async()
        return data

    @staticmethod
    def get_team_data(obj):
        return TeamSerializer(obj.team).data
