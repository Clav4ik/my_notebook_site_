from rest_framework import serializers
from ..models import Task

class TaskSerializers(serializers.ModelSerializer):
    title = serializers.CharField(required = True)
    task = serializers.CharField(required = True)
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'task' #, 'created_by', 'time_create','time_update'
        ]