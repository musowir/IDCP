# Generated by Django 4.1.1 on 2022-09-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0002_courseinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseinfo", name="hours_per_week", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="courseinfo", name="no_of_seats", field=models.IntegerField(),
        ),
    ]
