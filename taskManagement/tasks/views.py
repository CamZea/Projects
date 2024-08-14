from .serializers import AreaSerializer, TaskSerializer
from .models import Task, Area
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.

class AreaViewSet(ModelViewSet):
    queryset= Area.objects.all()
    serializer_class= AreaSerializer

class TaskViewSet(ModelViewSet):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer

