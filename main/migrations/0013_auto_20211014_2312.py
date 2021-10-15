# Generated by Django 3.2.7 on 2021-10-14 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20211014_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.user_info'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_info'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
