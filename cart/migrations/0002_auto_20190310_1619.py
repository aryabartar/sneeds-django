# Generated by Django 2.1.3 on 2019-03-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='public_classes',
            field=models.ManyToManyField(blank=True, null=True, to='classes.PublicClass'),
        ),
    ]
