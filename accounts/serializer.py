from rest_framework import serializers
from .models import Team, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'mobile', 'is_staff', 'is_active', 'is_superuser', 'role',
        )


class TeamSerializer(serializers.ModelSerializer):
    team_members_data = serializers.SerializerMethodField(required=False)
    team_leader_data = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Team
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', None)
        team_leader = data.get('team_leader', None)
        team_members = data.get('team_members', [])
        print(name,team_leader)
        print(team_members)
        if not name or not team_leader or  not team_members:
            raise serializers.ValidationError({'detail':'Name ,Team leader and Team members must be filled'})
        return data

    @staticmethod
    def get_team_members_data(obj):
        Team_member_data = []
        queryset = obj.team_members.all() if obj.team_members else None
        for member in queryset:
            Team_member_data.append(UserSerializer(member).data)
        return Team_member_data

    @staticmethod
    def get_team_leader_data(obj):
        return UserSerializer(obj.team_leader).data
