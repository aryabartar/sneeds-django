# Generated by Django 2.2.3 on 2020-04-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0007_remove_studyinfo_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyinfo',
            name='grade',
            field=models.CharField(choices=[('bachelor', 'Bachelor'), ('master', 'Master'), ('phd', 'Doctoral'), ('postdoc', 'Post Doc')], max_length=256),
        ),
    ]