from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TrainerViewSet, ExerciseViewSet, FitnessPlanViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'fitnessplans', FitnessPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
