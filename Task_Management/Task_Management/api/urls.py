"""
URL configuration for Task_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import TaskStatusUpdate
#from .views import TaskListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', views.TaskManagerListCreate.as_view(), name='create_task'),
    path('user/', views.UserListcreate.as_view(), name='add_user'),
    path('tasks/<int:id>/', views.TaskManagerDetailsUpdate.as_view(),name='retrieve_update_delete'),
    path('user/<int:id>/', views.UserDetailsUpdate.as_view(), name='retrieve_update_delete'),
    path('tasks/<int:id>/status/', TaskStatusUpdate.as_view(), name='task-status-update'),
    #path('tasks/', TaskListView.as_view(), name='task-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token


]  


    







