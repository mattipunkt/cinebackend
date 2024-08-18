# Generated by Django 5.1 on 2024-08-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(default='kein titel gegeben', max_length=120)),
                ('tmdb_filled', models.BooleanField(default=False)),
                ('tmdb_id', models.IntegerField(default='00000')),
                ('year', models.CharField(default='0000', max_length=4)),
                ('description', models.CharField(default='keine beschreibung angegeben', max_length=2000)),
                ('actors', models.CharField(default='Keine Schauspieler angegeben', max_length=120)),
                ('director', models.CharField(default='Kein regisseur angegeben', max_length=100)),
                ('use_in_carousel', models.BooleanField(default=False)),
            ],
        ),
    ]
