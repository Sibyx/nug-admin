# Generated by Django 4.0.4 on 2022-05-14 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_server_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='hostname',
            new_name='name',
        ),
    ]
