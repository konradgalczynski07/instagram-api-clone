from rest_framework import authentication, permissions, \
    viewsets, generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from core.models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Post a new post if authenticated or read only"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(author=self.request.user)


class AddCommentView(generics.CreateAPIView):
    """Add a new comment and edit or delete existing"""
    serializer_class = CommentSerializer
    # lookup_filed = 'post_id'
    # queryset = Comment.objects.filter(post=lookup_filed)
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self, **kwargs):
        print(self.request.query_params)
        post_id = self.request.query_params.get('post_id')

        # post_id = self.post_id
        # queryset = Comment.objects.filter(post=lookup_filed)

        return queryset
