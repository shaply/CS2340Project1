from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ResetPasswordView, ResetPasswordConfirmView

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),

    path('password-reset/', ResetPasswordView.as_view(), name='accounts.reset_password'),
    path('password-reset-confirm/<uidb64>/<token>/',
         ResetPasswordConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='accounts.password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='accounts.password_reset_complete'),
]