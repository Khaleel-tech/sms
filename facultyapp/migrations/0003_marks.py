# Generated by Django 5.0.7 on 2024-10-24 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_feedback'),
        ('facultyapp', '0002_alter_addcourse_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'), ('CTOD', 'COMPUTATIONAL THINKING FOR OBJECT DESIGN'), ('CTOOD', 'COMPUTATIONAL THINKING FOR OBJECT ORIENTED DESIGN'), ('PFSD', 'PYTHON FULL STACK WEB DEVELOPMENT'), ('DBMS', 'DATABASE MANAGEMENT SYSTEM'), ('DSS', 'DATA SCIENCE AND STATISTICS')], max_length=50)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]
