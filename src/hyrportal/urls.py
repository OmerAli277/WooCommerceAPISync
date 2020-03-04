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
	path('accounts/logout/', views.LogoutView.as_view(), name='logout'),

	path('accounts/', include('django.contrib.auth.urls')),
	#path('signup/', views.signup, name='signup'),
    path('accounts/login/request/', views.request, name='request'),
	# path('login/request/', views.request, name='request'),
	# path('', RedirectView.as_view(pattern_name='settings', permanent=False)),

	path('callback/' , views.callback , name='callback'),
	path('', views.home_page , name='home_page'),

    path('connect/', views.FortnoxSettingView.as_view(), name='connect'),

	path('fortnoxauth/', views.fortnoxauth, name='fortnoxauth'),
	path('settings/', views.SettingsView.as_view(), name='settings'),

	path('customer-settings/', views.CustomerSettingsView.as_view(), name = "customer-settings"),

	# path('connect/fortnox/update/' , views.FortnoxSettingView.as_view(), name='fortnox-update'),

    path('users/', views.UserListView.as_view(), name='user-list'),

    path('user/add/', views.signup, name='user-create'),
	# path('user/add/', views.UserCreateView.as_view(), name='user-create'),
	path('user/<int:pk>/edit/', views.UserEditView.as_view(), name='user-edit'),
	path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]
