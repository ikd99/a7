# Generated by Django 3.2.7 on 2021-10-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_requests_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='client_evaluation',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='driver_evaluation',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='matching_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requests',
            name='request_complete',
            field=models.BooleanField(default=False),
        ),
    ]