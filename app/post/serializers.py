from rest_framework import serializers
from core.models import Post, Comment
from django.contrib.auth import get_user_model
from django.db.models import Count


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for post's author info"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_pic')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the comment objects"""
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'posted_on')
        read_only_fields = ('author',)


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post objects"""
    author = AuthorSerializer(read_only=True)
    photo = serializers.ImageField(max_length=None, allow_empty_file=False)
    number_of_comments = serializers.SerializerMethodField()
    post_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author',  'photo',
                  'text', 'location', 'posted_on',
                  'number_of_comments', 'post_comments')

    def get_number_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()
