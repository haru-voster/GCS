from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Updated to use path instead of url
    path('', include('GRsystem.urls'))  # Updated to use path instead of url
]
