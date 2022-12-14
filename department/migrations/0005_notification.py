# Generated by Django 4.1.1 on 2022-09-14 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0004_rename_couse_code_courseinfo_course_code_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("publish_date", models.DateField(auto_created=True)),
                ("notification", models.CharField(max_length=400)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="department.depprofileinfo",
                    ),
                ),
            ],
        ),
    ]
