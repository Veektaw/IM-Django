# Generated by Django 4.2.3 on 2023-07-20 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_profile_f_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='f_name',
            new_name='first_name',
        ),
    ]
