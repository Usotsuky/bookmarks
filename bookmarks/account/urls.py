from django.urls import path
from . views import user_login, dashboard, edit, register
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),  # user_login
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),

    path('', dashboard, name='dashboard'),
]
