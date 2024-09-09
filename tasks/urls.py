from rest_framework.routers import DefaultRouter
from django.urls import path, include
from tasks.views import TaskViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),

]
