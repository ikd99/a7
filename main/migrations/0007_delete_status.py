# Generated by Django 3.2.7 on 2021-10-16 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_user_id_status_driver_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='status',
        ),
    ]
