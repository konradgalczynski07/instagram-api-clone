from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('<slug:username>/', views.UserProfileView.as_view(), name='user-profile'),
]
