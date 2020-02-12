# Generated by Django 2.2.3 on 2020-02-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('picture', models.ImageField(upload_to='images/account/country-pictures')),
                ('slug', models.SlugField(help_text='Lowercase pls', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='images/account/field-of-study-pictures')),
                ('slug', models.SlugField(help_text='Lowercase pls', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('country', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='images/account/university-pictures')),
                ('slug', models.SlugField(help_text='Lowercase pls', unique=True)),
            ],
        ),
    ]
