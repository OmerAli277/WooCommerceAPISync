"""hyrportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView
from .apps.core import views

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('token/', GetToken.as_view()),
	# path('users/', UsersViewSet.as_view()),
	# path('users/<int:pk>/', GetUserView.as_view()),
	# path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	# path('accounts/logout/', views.LogoutView.as_view(), name='logout'),

	path('accounts/', include('django.contrib.auth.urls')),
	path('signup/', views.signup, name='signup'),
	path('signup/creating', views.creating, name='creating'),
	# path('login/', views.login, name='login'),
	path('', RedirectView.as_view(pattern_name='settings', permanent=False)),
	path('settings/', views.SettingsView.as_view(), name='settings'),
	path('users/', views.UserListView.as_view(), name='user-list'),
	path('user/add/', views.UserCreateView.as_view(), name='user-create'),
	path('user/<int:pk>/edit/', views.UserEditView.as_view(), name='user-edit'),
	path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]
