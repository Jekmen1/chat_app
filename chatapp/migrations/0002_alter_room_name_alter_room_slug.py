# Generated by Django 5.0.2 on 2024-04-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
