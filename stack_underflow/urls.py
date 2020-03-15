from django.urls import path
from stack_underflow import views
app_name = 'stack_underflow'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('categories/', views.categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('logout/', views.user_logout, name='logout'),
]
