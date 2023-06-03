from django.urls import path
from .views import login_view, register_user, logout_view
from schedulers.views import scheduled_events


urlpatterns = [
    path('', scheduled_events, name="scheduled_events"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_view, name="logout")
]