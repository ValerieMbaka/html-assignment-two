from django.urls import path

# from the same location import views
from . import  views

app_name = 'app'
urlpatterns = [
        path('', views.index, name = "index"),
]