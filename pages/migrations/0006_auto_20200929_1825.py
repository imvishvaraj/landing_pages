# Generated by Django 3.1.1 on 2020-09-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='page-slug'),
        ),
    ]