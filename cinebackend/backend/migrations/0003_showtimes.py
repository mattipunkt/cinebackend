# Generated by Django 5.1 on 2024-08-16 17:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_movie_cover_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showtimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('collection', models.CharField(max_length=100, null=True)),
                ('language', models.CharField(default='dt. OV', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('premiere', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.movie')),
            ],
        ),
    ]
