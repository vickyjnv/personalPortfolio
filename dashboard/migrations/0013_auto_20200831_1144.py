# Generated by Django 3.0.3 on 2020-08-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20200831_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
