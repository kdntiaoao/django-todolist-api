from django.urls import include, path

from rest_framework import routers

from .views import (
    CreateUserView,
    PostListView,
    PostRetrieveView,
    TaskViewSet,
)

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostRetrieveView.as_view(), name="detail_post"),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]
