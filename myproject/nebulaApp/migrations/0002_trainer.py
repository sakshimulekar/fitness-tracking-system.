# Generated by Django 4.2.4 on 2023-08-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebulaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('specialization', models.CharField(choices=[('Yoga', 'Yoga'), ('Strength Training', 'Strength Training'), ('Cardio', 'Cardio'), ('Pilates', 'Pilates'), ('CrossFit', 'CrossFit'), ('Dance', 'Dance'), ('Functional Training', 'Functional Training'), ('Other', 'Other')], default='Other', max_length=50)),
                ('experience', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=11)),
            ],
        ),
    ]
