from rest_framework import viewsets, generics
from .models import User, Trainer, FitnessPlan, Exercise
from .serializers import UserSerializer, TrainerSerializer, FitnessPlanSerializer, ExerciseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class FitnessPlanViewSet(viewsets.ModelViewSet):
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanSerializer


class AddExerciseToFitnessPlan(APIView):
    def post(self, request, pk):
        try:
            fitness_plan = FitnessPlan.objects.get(pk=pk)
        except FitnessPlan.DoesNotExist:
            return Response({'detail': 'FitnessPlan not found'}, status=status.HTTP_404_NOT_FOUND)

        exercise_data = request.data
        exercise = Exercise.objects.create(**exercise_data)
        fitness_plan.exercises.add(exercise)
        serializer = FitnessPlanSerializer(fitness_plan)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateExerciseInFitnessPlan(APIView):
    def put(self, request, pk, exercise_pk):
        try:
            fitness_plan = FitnessPlan.objects.get(pk=pk)
            exercise = Exercise.objects.get(pk=exercise_pk)
        except (FitnessPlan.DoesNotExist, Exercise.DoesNotExist):
            return Response({'detail': 'FitnessPlan or Exercise not found'}, status=status.HTTP_404_NOT_FOUND)

        exercise_data = request.data
        for attr, value in exercise_data.items():
            setattr(exercise, attr, value)
        exercise.save()
        
        serializer = FitnessPlanSerializer(fitness_plan)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteExerciseFromFitnessPlan(APIView):
    def delete(self, request, pk, exercise_pk):
        try:
            fitness_plan = FitnessPlan.objects.get(pk=pk)
            exercise = Exercise.objects.get(pk=exercise_pk)
        except (FitnessPlan.DoesNotExist, Exercise.DoesNotExist):
            return Response({'detail': 'FitnessPlan or Exercise not found'}, status=status.HTTP_404_NOT_FOUND)

        fitness_plan.exercises.remove(exercise)
        exercise.delete()
        
        serializer = FitnessPlanSerializer(fitness_plan)
        return Response(serializer.data, status=status.HTTP_200_OK)