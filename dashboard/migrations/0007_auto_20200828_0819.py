# Generated by Django 3.0.3 on 2020-08-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_about_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('percent', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('percent', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ITConstructs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('percent', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('percent', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='SkillType',
        ),
    ]
