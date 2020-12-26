from django.urls import path
from . import views

app_name = 'hub'

urlpatterns = [

    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('home/<int:user>', views.home, name='home'),
    path('create', views.create, name='create'),
    path('create/<int:user>', views.home, name='create'),
    path('password_list', views.password_list, name='password_list'),
    path('password_list/<int:user>', views.password_list, name='password_list'),
    path('password_list/delete_data/', views.delete_data, name='delete_data'),
    
]
