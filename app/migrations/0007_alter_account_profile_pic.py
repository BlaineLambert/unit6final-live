# Generated by Django 4.2.6 on 2024-01-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_account_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='app/profilepics/user-default.jpeg', null=True, upload_to='app/profilepics/'),
        ),
    ]