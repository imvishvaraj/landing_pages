# Generated by Django 3.1.1 on 2020-09-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200929_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='page-slug'),
        ),
    ]
