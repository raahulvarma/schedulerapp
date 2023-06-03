from django.urls import path
from .views import scheduled_events, analytics, update_event, delete_event, add_event, edit_event


urlpatterns = [
    path('', scheduled_events, name="scheduled_events"),
    path('add_event/', add_event, name="add_event"),
    path('edit_event/<int:pk>/', edit_event, name="edit_event"),
    path('update_event/<int:pk>/', update_event, name="update_event"),
    path('delete_event/<int:pk>/', delete_event, name="delete_event"),
    path('analytics/', analytics, name="analytics"),
]