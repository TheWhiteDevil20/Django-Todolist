# Generated by Django 4.0.2 on 2022-12-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]