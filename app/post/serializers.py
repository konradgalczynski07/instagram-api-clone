from rest_framework import serializers
from core.models import Post, Comment
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for object author info"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_pic')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the comment objects"""
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'posted_on')
        read_only_fields = ('author', 'id', 'posted_on')


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post objects"""
    author = AuthorSerializer(read_only=True)
    photo = serializers.ImageField(max_length=None, allow_empty_file=False)
    number_of_comments = serializers.SerializerMethodField()
    post_comments = serializers.SerializerMethodField(
        'paginated_post_comments')
    liked_by_req_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author',  'photo',
                  'text', 'location', 'posted_on',
                  'number_of_likes', 'number_of_comments',
                  'post_comments', 'liked_by_req_user')

    def get_number_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()

    def paginated_post_comments(self, obj):
        page_size = 2
        paginator = Paginator(obj.post_comments.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1

        post_comments = paginator.page(page)
        serializer = CommentSerializer(post_comments, many=True)

        return serializer.data

    def get_liked_by_req_user(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()
