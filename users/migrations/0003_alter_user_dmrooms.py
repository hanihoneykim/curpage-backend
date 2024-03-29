# Generated by Django 4.1.7 on 2023-05-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dms", "0005_alter_dmroom_host_alter_dmroom_members"),
        ("users", "0002_user_dmrooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dmrooms",
            field=models.ManyToManyField(related_name="user_dmrooms", to="dms.dmroom"),
        ),
    ]
