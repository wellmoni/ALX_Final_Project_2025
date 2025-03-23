from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)  
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'





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

    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='username')  
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(max_length=15, choices=PRIORITY, default='low')
    status = models.CharField(max_length=15, choices=STATUS, default='pending')
    completed_at = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
       
        if self.status == 'completed' and self.completed_at is None:
            from django.utils.timezone import now
            self.completed_at = now()
        elif self.status == 'pending':
            self.completed_at = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.username.username}"

   

# Create your models here.





