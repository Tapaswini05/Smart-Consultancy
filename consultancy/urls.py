from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('loginpage/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('disease/', views.disease, name='disease'),
    path('consult/', views.consult, name='consult'),
    path('about/', views.about, name='about'),
    path('logout/', views.logoutuser, name='logout'),
    path('derma/', views.derma, name='derma'),
    path('gyno/', views.gyno, name='gyno'),
    path('consultnow/', views.consultnow, name='consultnow'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),




]

