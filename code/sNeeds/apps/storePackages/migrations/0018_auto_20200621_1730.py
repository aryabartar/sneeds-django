# Generated by Django 2.2.3 on 2020-06-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storePackages', '0017_auto_20200621_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storepackagephase',
            name='phase_details',
            field=models.ManyToManyField(blank=True, to='storePackages.StorePackagePhaseDetail'),
        ),
    ]
