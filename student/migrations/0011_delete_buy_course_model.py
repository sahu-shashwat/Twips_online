# Generated by Django 5.0 on 2023-12-13 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_rename_order_id_buy_course_model_orderid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buy_course_model',
        ),
    ]
