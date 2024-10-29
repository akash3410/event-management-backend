from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("events/add/", views.add_events, name="add_events"),
    path('signup/', views.registration, name="registration"),
    path('login/', views.signIn, name="signIn"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name="profile"),
    path('event/details/<int:event_id>/', views.event_details, name="event_details"),
    path('event/update/<int:event_id>/', views.update_event, name="update_event"),
    path('event/delete/<int:event_id>/', views.delete_event, name="delete_event"),
]