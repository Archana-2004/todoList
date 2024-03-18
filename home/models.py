from django.db import models

# Create your models here.
class Task(models.Model):

    class Meta:
        app_label = 'home'
    taskTitle=models.CharField(max_length=30)
    taskDesc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.taskTitle)
    
