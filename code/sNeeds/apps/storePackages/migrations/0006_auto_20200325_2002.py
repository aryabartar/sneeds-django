# Generated by Django 2.2.3 on 2020-03-25 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0003_auto_20200309_1356'),
        ('storePackages', '0005_consultantacceptsoldproductrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantSoldStorePackageAcceptRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultants.ConsultantProfile')),
                ('sold_store_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storePackages.SoldStorePackage')),
            ],
            options={
                'unique_together': {('sold_store_package', 'consultant')},
            },
        ),
        migrations.DeleteModel(
            name='ConsultantAcceptSoldProductRequest',
        ),
    ]
