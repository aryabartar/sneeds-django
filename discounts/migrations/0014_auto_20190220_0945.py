# Generated by Django 2.1.3 on 2019-02-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0013_auto_20190220_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeprofile',
            name='cafe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_profile', to='discounts.Cafe'),
        ),
    ]