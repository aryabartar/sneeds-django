# Generated by Django 2.1.3 on 2019-02-11 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0010_auto_20190210_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='discount_info',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='userdiscount',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userdiscount',
            name='status',
            field=models.CharField(choices=[('not_used', 'استفاده نشده'), ('used', 'استفاده شده')], default='not_used', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdiscount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_discounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useruseddiscount',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_used_discounts', to='discounts.Cafe'),
        ),
    ]
