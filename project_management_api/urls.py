from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"projects", ProjectViewSet, basename="project")

projects_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
projects_router.register(r"tasks", TaskViewSet, basename="project-tasks")

tasks_router = routers.NestedDefaultRouter(projects_router, r"tasks", lookup="task")
tasks_router.register(r"comments", CommentViewSet, basename="task-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
    path("", include(tasks_router.urls)),
    # JWT Token endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
