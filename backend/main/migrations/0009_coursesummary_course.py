# Generated by Django 4.0.1 on 2022-11-04 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_coursesummary_isverified'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesummary',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='main.courselist'),
        ),
    ]
