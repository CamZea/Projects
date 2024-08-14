from .models import Task, Area
from rest_framework.serializers import ModelSerializer
class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields= '__all__'

class AreaSerializer(ModelSerializer):
    class Meta:
        model= Area
        fields= (
            'id',
            'title',
            'description',
            'user'
        )