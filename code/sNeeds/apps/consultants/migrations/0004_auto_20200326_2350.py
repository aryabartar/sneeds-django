# Generated by Django 2.2.3 on 2020-03-26 19:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0003_auto_20200309_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='bio',
            field=ckeditor.fields.RichTextField(default='default'),
        ),
    ]
