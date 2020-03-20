from django.urls import path, include
from stack_underflow import views
app_name = 'stack_underflow'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_thread/', views.add_thread, name='add_thread'),
    path('category/<slug:thread_question_slug>/show_thread/', views.show_thread, name='show_thread'),
    path('category/<slug:thread_question_slug>/add_reply/', views.add_reply, name='add_reply'),
    path('categories/', views.categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('logout/', views.user_logout, name='logout'),
]
