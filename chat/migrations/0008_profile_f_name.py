# Generated by Django 4.2.3 on 2023-07-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_profile_id_user_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='f_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]