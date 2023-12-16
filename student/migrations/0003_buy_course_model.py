# Generated by Django 5.0 on 2023-12-12 12:20

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('student', '0002_student_model_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_course_model',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.CharField(max_length=30)),
                ('order_name', models.CharField(max_length=50)),
                ('bought_date', models.DateField()),
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
