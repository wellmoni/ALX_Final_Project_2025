from rest_framework import serializers
from .models import Task, CustomUser


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


    def update(self, instance, validated_data):
        
        if instance.status == 'completed' and 'status' not in validated_data:
            raise serializers.ValidationError("You cannot edit a completed task unless you change its status to 'pending'.")

        return super().update(instance, validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = CustomUser
        fields = '__all__' #('id', 'username', 'email', 'password')



