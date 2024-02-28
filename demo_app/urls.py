from django.urls import path
from demo_app import views

app_name = "demo_app"

urlpatterns = [
    path('', views.home, name = "home"),
    
]