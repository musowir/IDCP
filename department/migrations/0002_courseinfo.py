# Generated by Django 4.1.1 on 2022-09-07 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseInfo",
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
                ("couse_code", models.CharField(max_length=15, unique=True)),
                ("couse_name", models.CharField(max_length=200)),
                ("start_date", models.DateField()),
                (
                    "slot",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                        ],
                        default="E",
                        max_length=5,
                    ),
                ),
                ("hours_per_week", models.IntegerField(max_length=5)),
                ("no_of_seats", models.IntegerField(max_length=3)),
                ("syllabus", models.FileField(upload_to="uploads/")),
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