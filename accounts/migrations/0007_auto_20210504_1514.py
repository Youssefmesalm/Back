# Generated by Django 3.1.7 on 2021-05-04 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
