from django.contrib import admin
from django.urls import path, include
from savings import views  # Import the views module from your savings app

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('admin/', admin.site.urls),
    path('savings/', include('savings.urls')),
]
