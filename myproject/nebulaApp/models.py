from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    GENDER_SELECT = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    SPECIALIZATION_CHOICES = (
        ('Yoga', 'Yoga'),
        ('Strength Training', 'Strength Training'),
        ('Cardio', 'Cardio'),
        ('Pilates', 'Pilates'),
        ('CrossFit', 'CrossFit'),
        ('Dance', 'Dance'),
        ('Functional Training', 'Functional Training'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,choices=GENDER_SELECT)
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES,default='Other')
    experience=models.PositiveIntegerField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()

class FitnessPlan(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.CharField(max_length=200)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name



