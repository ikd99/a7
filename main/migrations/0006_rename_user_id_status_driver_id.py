# Generated by Django 3.2.7 on 2021-10-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='user_id',
            new_name='driver_id',
        ),
    ]
