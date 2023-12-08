# Generated by Django 5.0 on 2023-12-07 12:22

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_model',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('roll_number', models.CharField(max_length=10)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('date_of_birth', models.DateField()),
                ('stream', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH'), ('EEE', 'EEE'), ('CIVIL', 'CIVIL'), ('IT', 'IT')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
