# Generated by Django 4.0.10 on 2023-10-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0004_alter_text_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(default='', max_length=225, verbose_name='제목'),
        ),
    ]
