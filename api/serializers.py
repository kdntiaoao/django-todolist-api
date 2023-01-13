from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content", "created_at", "updated_at")

    def get_author(self, instance):
        return UserSerializer(instance.author).data["username"]


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ("id", "user", "title", "created_at", "updated_at")

    def get_user(self, instance):
        return UserSerializer(instance.user).data["username"]


class CreateTaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ("id", "user", "title", "created_at", "updated_at")
