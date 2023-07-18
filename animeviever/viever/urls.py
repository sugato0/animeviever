from django.urls import path
from .views import *

urlpatterns = [
    
    path('videos/<int:series_id>/', video_list, name='video_list'),
    
]