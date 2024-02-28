from django.urls import path
from second_app import views

app_name = "second_app"

urlpatterns = [
    path('', views.index, name = "index"),
    
]