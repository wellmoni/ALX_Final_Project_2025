from rest_framework import viewsets, permissions
from .models import Task, CustomUser  
from .serializers import TaskSerializer, CustomUserSerializer
from datetime import date
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        due_date = serializer.validated_data.get("due_date")
        if due_date and due_date.date() < date.today():
            return Response({"error": "Due date must be in the future."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()


# Create your views here.
