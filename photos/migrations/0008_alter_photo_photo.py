# Generated by Django 4.0.10 on 2023-10-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.URLField(default='', max_length=500, null=True, verbose_name='사진파일'),
        ),
    ]
