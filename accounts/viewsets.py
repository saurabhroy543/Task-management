from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import AdminPerm
from .models import Team
from .serializer import TeamSerializer
from rest_framework.viewsets import ModelViewSet


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AdminPerm]

    def get_queryset(self):
        queryset = super(TeamViewSet, self).get_queryset()
        return queryset
