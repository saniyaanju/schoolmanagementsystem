# Generated by Django 5.0.1 on 2024-02-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(default=1),
        ),
    ]
