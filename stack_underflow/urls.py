from django.urls import path
from stack_underflow import views
app_name = 'stack_underflow'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('categories/', views.categories, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
