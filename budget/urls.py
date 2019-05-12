
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/profile/', views.project_list, name='list'),
    path('', LoginView.as_view(template_name='budget/accounts/login.html'), name="login"),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail'),
    path('accounts/login/', LoginView.as_view(template_name='budget/accounts/login.html'), name="login"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/logout/', LogoutView.as_view(template_name='budget/accounts/logout.html'), name="logout")
]
