from django.contrib import admin
from django.urls import path, include
from accounts import views
from accounts.views import user_list

urlpatterns = [
 path("register", views.register, name="register"),
 path("login", views.login, name="login"),
 path("logout",views.logout, name='logout'),
 path("view_list", views.user_list, name='user_list'),
 path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
 path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

]
