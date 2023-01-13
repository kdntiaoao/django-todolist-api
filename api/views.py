from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    PostSerializer,
    TaskSerializer,
    CreateTaskSerializer,
)
from .models import Post, Task


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("user").all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateTaskSerializer
        return TaskSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = (AllowAny,)
            return [permission() for permission in permission_classes]
        return super().get_permissions()
