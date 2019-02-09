from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token


from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(),
         name='register'),
    path('login/', obtain_jwt_token,
         name='login'),
    path('me/', views.ManageUserView.as_view(),
         name='me'),
    path('<slug:username>/', views.UserProfileView.as_view(),
         name='user-profile'),
    path('<slug:username>/follow/', views.FollowUserView.as_view(),
         name='follow-user'),
    path('<slug:username>/get-followers/', views.GetFollowersView.as_view(),
         name='get-followers'),
    path('<slug:username>/get-following/', views.GetFollowingView.as_view(),
         name='get-following'),
]
