# Generated by Django 4.1.1 on 2022-11-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]