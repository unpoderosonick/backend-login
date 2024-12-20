# Generated by Django 5.1.4 on 2024-12-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firebase_uid', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('language', models.CharField(default='en', max_length=10)),
                ('timezone', models.CharField(default='UTC', max_length=50)),
            ],
        ),
    ]
