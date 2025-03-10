from django.urls import path
from . import views
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, EventListView, EventCreateView

urlpatterns = [
    # Category URLs...............
    # path('categories/', views.category_list, name='category_list'),
    # path('categories/new/', views.category_create, name='category_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    # path('categories/edit/<int:pk>/', views.category_update, name='category_update'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    # path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Event URLs..................
    # path('events/', views.event_list, name='event_list'),
    # path('events/new/', views.event_create, name='event_create'),
     path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/edit/<int:pk>/', views.event_update, name='event_update'),
    path('events/delete/<int:pk>/', views.event_delete, name='event_delete'),

    # Participant URLs...............
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/new/', views.participant_create, name='participant_create'),
    path('participants/edit/<int:pk>/', views.participant_update, name='participant_update'),
    path('participants/delete/<int:pk>/', views.participant_delete, name='participant_delete'),
]
