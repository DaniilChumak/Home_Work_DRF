# Generated by Django 5.1 on 2024-09-03 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите курс",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
