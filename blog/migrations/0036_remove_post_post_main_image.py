# Generated by Django 2.1.3 on 2019-03-01 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20190301_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_main_image',
        ),
    ]
