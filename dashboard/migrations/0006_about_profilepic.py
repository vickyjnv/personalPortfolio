# Generated by Django 3.0.3 on 2020-08-28 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200828_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profilePic',
            field=models.ImageField(blank=True, upload_to='images/profile/'),
        ),
    ]