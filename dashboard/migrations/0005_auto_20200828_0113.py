# Generated by Django 3.0.3 on 2020-08-27 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200828_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='codingskill',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(default='#'),
        ),
    ]