# Generated by Django 5.0.2 on 2024-02-12 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bumpevent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('username_1', models.CharField(blank=True, max_length=50)),
                ('username_2', models.CharField(blank=True, max_length=50)),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_one_matches', to=settings.AUTH_USER_MODEL)),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_two_matches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]