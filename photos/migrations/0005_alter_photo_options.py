# Generated by Django 4.1.7 on 2023-06-14 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0004_alter_photo_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photo",
            options={"ordering": ["-created_at"]},
        ),
    ]