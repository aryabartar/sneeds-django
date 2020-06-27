# Generated by Django 2.2.3 on 2020-06-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storePackages', '0021_storepackagephase_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storepackagephase',
            name='status',
        ),
        migrations.AddField(
            model_name='storepackagephasedetail',
            name='status',
            field=models.CharField(choices=[('not_started', 'شروع نشده'), ('in_progress', 'در حال انجام'), ('done', 'انجام شد'), ('finished', 'دریافت نتیجه'), ('pending_user_data', 'دریافت اطلاعات کاربر')], default='not_started', max_length=1024),
        ),
    ]
