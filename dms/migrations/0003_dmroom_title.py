# Generated by Django 4.1.7 on 2023-05-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dms", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dmroom",
            name="title",
            field=models.CharField(default="", max_length=15),
        ),
    ]