# Generated by Django 2.2.3 on 2020-03-26 13:20

from django.db import migrations
import sNeeds.apps.discounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0012_auto_20200326_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='code',
            field=sNeeds.apps.discounts.models.CICharField(blank=True, help_text='If want to populate automatically, Leave this field blank. Otherwise enter code', max_length=128, unique=True),
        ),
    ]
