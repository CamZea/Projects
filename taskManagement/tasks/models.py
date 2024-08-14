from django.db import models
from users.models import User

# Create your models here.
class Area(models.Model):
    title= models.CharField(max_length=150, blank=True)
    description= models.CharField(max_length=255, null= True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table= 'tasks_area'

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    name= models.CharField(max_length=100)
    area=models.ForeignKey(
        Area, on_delete=models.CASCADE, null= True, blank=True
    )
    user=models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank= True
    )
    description= models.TextField(null=True, blank=True)
    status= models.CharField(
        null= True,
        blank=True,
        choices=[
            ('created', 'Creado'),
            ('in_progress', 'En proceso'),
            ('finished', 'Finalizado')

        ]
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tasks'
    


   