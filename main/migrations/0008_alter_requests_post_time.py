# Generated by Django 3.2.7 on 2021-10-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
