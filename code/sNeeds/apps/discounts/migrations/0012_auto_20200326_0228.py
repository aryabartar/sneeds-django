# Generated by Django 2.2.3 on 2020-03-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0011_auto_20200325_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='use_limit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
