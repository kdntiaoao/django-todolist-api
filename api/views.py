from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    BasePermission,
    IsAuthenticated,
    SAFE_METHODS,
)
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    PostSerializer,
    CreatePostSerializer,
    TaskSerializer,
    CreateTaskSerializer,
)
from .models import Post, Task


class IsAuthorOrIsAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreatePostSerializer
        return PostSerializer


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
        if self.action in ("list", "retrieve"):
            permission_classes = (IsAuthenticated,)
            return [permission() for permission in permission_classes]
        elif self.action in ("update", "partial_update", "destroy"):
            permission_classes = (IsAuthorOrIsAuthenticated,)
            return [permission() for permission in permission_classes]
        return super().get_permissions()
