
from django.contrib import admin
from django.urls import path, include
from events.views import organizer_dashboard 

urlpatterns = [
    
    path('', organizer_dashboard, name='organizer_dashboard'),  
    path('admin/', admin.site.urls),  
    path('events/', include('events.urls')),  
]

