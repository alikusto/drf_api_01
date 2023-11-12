from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import Post, Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Post
        fields = '__all__'


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
