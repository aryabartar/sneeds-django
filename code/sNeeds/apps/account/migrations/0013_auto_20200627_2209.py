# Generated by Django 2.2.3 on 2020-06-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200627_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentformfieldschoice',
            name='slug',
            field=models.SlugField(help_text='Lowercase pls', unique=True),
        ),
    ]
