# Generated by Django 5.0 on 2023-12-20 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_opt_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='opt_model',
            new_name='otp_model',
        ),
        migrations.RenameField(
            model_name='otp_model',
            old_name='opt_no',
            new_name='otp_no',
        ),
    ]
