# Generated by Django 2.2.4 on 2019-08-08 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='screen',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
