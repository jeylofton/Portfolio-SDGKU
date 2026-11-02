from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/add/', views.add_project, name='add_project'),
    path('skills/', views.skill_list, name='skill_list'),
]
