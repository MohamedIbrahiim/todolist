# Generated by Django 4.0.2 on 2022-02-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={},
        ),
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]