# Generated by Django 2.2.3 on 2020-03-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20200228_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tag',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]