# Generated by Django 4.2.6 on 2024-01-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_account_profile_pic_alter_properties_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='app/uploads/default.png', null=True, upload_to='app/uploads/'),
        ),
    ]
