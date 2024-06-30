# Generated by Django 5.0 on 2023-12-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_buy_course_model_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy_course_model',
            name='bought_date',
        ),
        migrations.AlterField(
            model_name='buy_course_model',
            name='course_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='buy_course_model',
            name='sid',
            field=models.PositiveIntegerField(),
        ),
    ]