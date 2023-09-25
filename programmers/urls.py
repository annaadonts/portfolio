from django.urls import path
from . import views

urlpatterns = [
    path('', views.programmer_list, name='programmer_list'),
    path('add_programmer/', views.add_programmer, name='add_programmer'),
    path('<int:programmer_id>/', views.programmer_detail, name='programmer_detail'),
    path('<int:programmer_id>/add_project/', views.add_project, name='add_project'),
]
