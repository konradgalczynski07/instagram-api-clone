from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post import views


router = DefaultRouter()
router.register('', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('feed/',
         views.UserFeedView.as_view(),
         name='feed'),
    path('', include(router.urls)),
    path('comment/<uuid:post_id>/',
         views.AddCommentView.as_view(),
         name='add-comment'),
    path('comment/<int:comment_id>/',
         views.ManageCommentView.as_view(),
         name='manage-comment'),
    path('like/<uuid:post_id>/',
         views.LikeView.as_view(),
         name='like'),
    path('<uuid:post_id>/get-likers/',
         views.GetLikersView.as_view(),
         name='get-likers'),
]
