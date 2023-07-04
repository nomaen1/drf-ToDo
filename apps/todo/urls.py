from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.todo.views import ToDoAPIViewSet

router = DefaultRouter()
router.register("todo", ToDoAPIViewSet, "api_todo")

urlpatterns = router.urls