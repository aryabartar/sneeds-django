# Generated by Django 2.2.3 on 2020-02-28 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200214_1549'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminComment',
        ),
    ]
