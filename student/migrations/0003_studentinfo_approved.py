# Generated by Django 4.1.1 on 2022-10-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_alter_studentinfo_exam_reg_no_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentinfo",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]