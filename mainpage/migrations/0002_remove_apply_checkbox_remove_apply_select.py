# Generated by Django 4.0.4 on 2022-05-28 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='checkbox',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='select',
        ),
    ]
