# Generated by Django 3.2.7 on 2021-10-15 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='client_evaluation',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='driver_evaluation',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='matching_complete',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='request_complete',
        ),
    ]