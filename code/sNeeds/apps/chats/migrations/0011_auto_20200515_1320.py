# Generated by Django 2.2.3 on 2020-05-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_auto_20200515_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmessage',
            name='text_message',
            field=models.TextField(),
        ),
    ]
