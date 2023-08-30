from rest_framework import serializers
from .models import User, Trainer, FitnessPlan, Exercise
from rest_framework import generics

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class FitnessPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = FitnessPlan
        fields = '__all__'

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        fitness_plan = FitnessPlan.objects.create(**validated_data)
        for exercise_data in exercises_data:
            exercise = Exercise.objects.create(**exercise_data)
            fitness_plan.exercises.add(exercise)
        return fitness_plan
