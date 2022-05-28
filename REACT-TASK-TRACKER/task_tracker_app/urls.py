from django.urls import path
from .views import TaskList, TaskDetail, Home

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('list/', TaskList.as_view(), name='tasklist'),
    path('<int:pk>/', TaskDetail.as_view(), name='tasklist'),
]
