from django.urls import path

from .api_views import TaskListAPIView

urlpatterns = [
    path('apitask', TaskListAPIView.as_view(), name = 'apitask')
]
