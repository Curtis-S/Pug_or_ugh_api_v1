# Generated by Django 2.1.1 on 2018-09-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0008_auto_20180915_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(max_length=1),
        ),
    ]
