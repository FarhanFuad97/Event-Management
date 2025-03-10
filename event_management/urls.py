from django.contrib import admin
from django.urls import path, include
from events.views import organizer_dashboard,home_view, dashboard
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", home_view, name="home"),  
    path("dashboard/", organizer_dashboard, name="organizer_dashboard"),  
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),  
    path("users/", include("users.urls")),
    path('dashboard', dashboard, name='dashboard')   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










