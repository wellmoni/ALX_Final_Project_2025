from rest_framework import viewsets, permissions, generics
from .models import Task, CustomUser  
from .serializers import TaskSerializer, CustomUserSerializer
from datetime import date
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, status
from rest_framework.views import APIView
from django.utils.timezone import now
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated



class TaskManagerListCreate(generics.ListCreateAPIView):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]

#class TaskListView(generics.ListAPIView):
 #   queryset =Task.objects.all()
  #  serializer_class = TaskSerializer
   # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority_level', 'due_date']  # Filters
    ordering_fields = ['due_date', 'priority_level']  # Sorting options


class UserListcreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class TaskManagerDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class =TaskSerializer
    lookup_url_kwarg = 'id'


class UserDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_url_kwarg = 'id'
    

class TaskStatusUpdate(APIView):
    
    
    def patch(self, request, id):
        try:
            task = Task.objects.get(id=id)

           
            new_status = request.data.get('status')

            
            if new_status not in ['pending', 'completed']:
                return Response({"error": "Invalid status. Choose 'pending' or 'completed'."}, status=status.HTTP_400_BAD_REQUEST)

           
            if task.status == 'completed' and new_status == 'completed':
                return Response({"error": "Task is already completed."}, status=status.HTTP_400_BAD_REQUEST)

            
            task.status = new_status
            task.completed_at = now() if new_status == 'completed' else None
            task.save()

            return Response({"message": f"Task marked as {new_status}."}, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)




    # Create your views here.
