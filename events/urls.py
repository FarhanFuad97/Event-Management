from django.urls import path
from . import views
from events.views import organizer_dashboard  

urlpatterns = [
    path('', organizer_dashboard, name='organizer_dashboard'),
    
]

urlpatterns = [
    # Category URLs...............
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Event URLs..................
    path('events/', views.event_list, name='event_list'),
    path('events/new/', views.event_create, name='event_create'),
    path('events/edit/<int:pk>/', views.event_update, name='event_update'),
    path('events/delete/<int:pk>/', views.event_delete, name='event_delete'),

    # Participant URLs...............
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/new/', views.participant_create, name='participant_create'),
    path('participants/edit/<int:pk>/', views.participant_update, name='participant_update'),
    path('participants/delete/<int:pk>/', views.participant_delete, name='participant_delete'),
]
