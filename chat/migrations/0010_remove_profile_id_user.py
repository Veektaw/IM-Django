# Generated by Django 4.2.3 on 2023-07-21 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_rename_f_name_profile_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]