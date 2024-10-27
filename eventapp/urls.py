from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("events/", views.all_events, name="all_events"),
    path("events/add/", views.add_events, name="add_events"),
    path('signup/', views.registration, name="registration"),
    path('login/', views.signIn, name="signIn"),
]