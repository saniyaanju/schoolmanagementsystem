# Generated by Django 5.0.1 on 2024-02-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_fees_alter_student_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cls',
            field=models.IntegerField(default=1),
        ),
    ]
