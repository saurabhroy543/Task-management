from .models import Task
from .permissions import TaskPerm
from .serializer import TaskSerializer
from rest_framework.viewsets import ModelViewSet


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [TaskPerm]
