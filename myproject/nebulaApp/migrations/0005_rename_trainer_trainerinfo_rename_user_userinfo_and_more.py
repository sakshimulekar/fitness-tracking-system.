# Generated by Django 4.2.4 on 2023-09-01 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nebulaApp', '0004_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trainer',
            new_name='TrainerInfo',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
