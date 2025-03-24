from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='dashboard-home'),
     path('index_new', views.index_new, name='index_new'),
     path('create_new_project', views.create_new_project, name='create_new_project')
]
