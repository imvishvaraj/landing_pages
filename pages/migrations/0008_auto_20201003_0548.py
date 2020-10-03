# Generated by Django 3.1.1 on 2020-10-03 05:48

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_page_leave_capture'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='jumbtron_bg_color',
            field=models.CharField(default='#eeeeee', max_length=7, validators=[pages.models.layout_validators]),
        ),
        migrations.AddField(
            model_name='page',
            name='jumbtron_text_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validators]),
        ),
    ]
