# Generated by Django 3.2.7 on 2021-10-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='requests',
            name='photo',
            field=models.ImageField(default='defo', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
