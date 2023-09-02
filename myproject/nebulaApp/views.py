from rest_framework import viewsets, generics
from .models import UserInfo, TrainerInfo, FitnessPlan, Exercise
from .serializers import UserSerializer, TrainerSerializer, FitnessPlanSerializer, ExerciseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserRegisterSerializer
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = TrainerInfo.objects.all()
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
    

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = serializer.save()
                login(request, user)  # Log in the user
                return Response({'msg': 'Registration successful','user':serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if user.password == password:  # Check if the provided password matches the stored password
            login(request, user)
            serializer = UserRegisterSerializer(user)
            return Response({'user': serializer.data, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
