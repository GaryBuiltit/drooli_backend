# Generated by Django 4.1.5 on 2023-02-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drooli', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='age',
        ),
    ]
