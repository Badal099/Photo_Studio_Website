# Generated by Django 3.0.3 on 2021-03-29 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudioApp', '0008_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='msg',
            new_name='message',
        ),
    ]
