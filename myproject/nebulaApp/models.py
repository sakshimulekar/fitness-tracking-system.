from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission;

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     username = None
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_trainer = models.BooleanField(default=False)
    username = models.CharField(
        max_length=150,
        unique=True,  # Unique constraint to ensure usernames are unique
        blank=True,   # Allow empty usernames
    )
    groups = models.ManyToManyField(Group, related_name="custom_users")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_users")

# Create your models here.
class UserInfo(models.Model):
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
    image = models.URLField(default='https://cdn-icons-png.flaticon.com/512/5087/5087579.png',blank=True,)  # Allow the field to be empty)
    contact_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    

class TrainerInfo(models.Model):
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
    image = models.URLField(default='https://cdn-icons-png.flaticon.com/512/5087/5087579.png',blank=True,)  # Allow the field to be empty)
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


