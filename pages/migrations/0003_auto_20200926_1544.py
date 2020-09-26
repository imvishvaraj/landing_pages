# Generated by Django 3.1.1 on 2020-09-26 15:44

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200926_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validators]),
        ),
    ]
