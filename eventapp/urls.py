from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path('event/details/<int:event_id>/', views.event_details, name="event_details"),
    path("events/add/", views.add_events, name="add_events"),
    path('signup/', views.registration, name="registration"),
    path('accounts/login/', views.signIn, name="signIn"),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name="profile"),
    path('event/update/<int:event_id>/', views.update_event, name="update_event"),
    path('event/delete/<int:event_id>/', views.delete_event, name="delete_event"),
    path('user/update/', views.user_update, name="user_update"),
    path('event/booking/<int:event_id>/', views.book_event, name='book_event'),
    path('event/booked/', views.bokked_events, name='bokked_events'),
    path('event/booked/cancel/<int:event_id>/', views.cancel_booking, name='cancel_booking'),
]