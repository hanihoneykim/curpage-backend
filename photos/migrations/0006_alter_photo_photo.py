# Generated by Django 4.0.10 on 2023-10-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(default='', null=True, upload_to='', verbose_name='사진파일'),
        ),
    ]
