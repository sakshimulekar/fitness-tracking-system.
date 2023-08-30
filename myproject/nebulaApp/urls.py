from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TrainerViewSet, ExerciseViewSet, FitnessPlanViewSet
from .views import AddExerciseToFitnessPlan, UpdateExerciseInFitnessPlan, DeleteExerciseFromFitnessPlan

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'fitnessplans', FitnessPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fitnessplans/<int:pk>/add_exercise/', AddExerciseToFitnessPlan.as_view(), name='add-exercise-to-fitnessplan'),
    path('fitnessplans/<int:pk>/update_exercise/<int:exercise_pk>/', UpdateExerciseInFitnessPlan.as_view(), name='update-exercise-in-fitnessplan'),
    path('fitnessplans/<int:pk>/delete_exercise/<int:exercise_pk>/', DeleteExerciseFromFitnessPlan.as_view(), name='delete-exercise-from-fitnessplan'),
]
