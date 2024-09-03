# Generated by Django 5.1 on 2024-09-03 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "title",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=100,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview_image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку для превью курса",
                        null=True,
                        upload_to="materials/courses/previews/",
                        verbose_name="Картинка",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание курса",
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "title",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=100,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание урока",
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview_image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку для превью курса",
                        null=True,
                        upload_to="materials/lessons/previews/",
                        verbose_name="Картинка",
                    ),
                ),
                (
                    "link_to_video",
                    models.CharField(
                        blank=True,
                        help_text="Укажите ссылку на видео",
                        max_length=150,
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="Выберите курс",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
