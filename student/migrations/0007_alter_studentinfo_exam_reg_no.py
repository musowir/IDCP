# Generated by Django 4.1.1 on 2022-11-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_attendance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentinfo",
            name="exam_reg_no",
            field=models.CharField(max_length=12),
        ),
    ]
