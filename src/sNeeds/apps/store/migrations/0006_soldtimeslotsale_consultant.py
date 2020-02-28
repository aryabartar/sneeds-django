# Generated by Django 2.2.3 on 2020-02-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0001_initial'),
        ('store', '0005_auto_20200221_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='consultant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='customAuth.ConsultantProfile'),
            preserve_default=False,
        ),
    ]