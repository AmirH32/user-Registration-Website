# Generated by Django 4.1 on 2022-08-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='Enter', max_length=500),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='Enter', max_length=100),
        ),
    ]