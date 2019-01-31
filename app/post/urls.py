from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post import views


router = DefaultRouter()
router.register('posts', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
    path('comment/<uuid:post_id>',
         views.AddCommentView.as_view(),
         name='add-comment'),
    # path('comment/<uuid:post_id>/<int:comment_id>', views.ManageCommentView.as_view(), name='manage-comment'),
]
