# Generated by Django 5.0 on 2023-12-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_chat_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_model',
            name='course_id',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
