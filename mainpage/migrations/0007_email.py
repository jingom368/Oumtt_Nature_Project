# Generated by Django 4.0.4 on 2022-05-31 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_rename_checkbox_2_apply_piagree_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
