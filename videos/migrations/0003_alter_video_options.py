# Generated by Django 4.1.7 on 2023-06-14 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0002_alter_video_video"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="video",
            options={"ordering": ["-created_at"]},
        ),
    ]