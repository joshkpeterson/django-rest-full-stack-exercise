# Generated by Django 3.1 on 2020-08-24 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='roles',
            new_name='role',
        ),
    ]
