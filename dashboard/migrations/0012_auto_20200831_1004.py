# Generated by Django 3.0.3 on 2020-08-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200828_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about2',
            field=models.TextField(blank=True),
        ),
    ]