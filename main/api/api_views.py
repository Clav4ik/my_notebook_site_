from rest_framework.generics import ListAPIView

from ..models import Task
from .serializers import TaskSerializers


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()