# Generated by Django 5.0.2 on 2024-02-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_bumpevent_server_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(default='../../img/portrait-0.png', max_length=250),
        ),
    ]
