# Generated by Django 4.0.4 on 2022-05-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_apply_checkbox_alter_apply_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='checkbox',
            field=models.TextField(null=True),
        ),
    ]
