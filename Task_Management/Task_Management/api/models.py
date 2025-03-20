from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)



def __str__(self):
        return self.username



class Task(models.Model):
    PRIORITY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks")  
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority_level = models.CharField(max_length=15, choices=PRIORITY, default='medium')
    status = models.CharField(max_length=15, choices=STATUS, default='pending')

    def __str__(self):
        return f"{self.title} - {self.user.username}"

# Create your models here.




# Create your models here.
