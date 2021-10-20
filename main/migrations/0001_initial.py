# Generated by Django 3.2.8 on 2021-10-19 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_driver', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=50)),
                ('total_socore', models.FloatField(max_length=50)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('matching_complete', models.BooleanField(default=False)),
                ('request_complete', models.BooleanField(default=False)),
                ('payment', models.BooleanField(default=False)),
                ('share_or_not', models.BooleanField(default=False)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=1000)),
                ('departure_place', models.CharField(max_length=100)),
                ('destination_place', models.CharField(max_length=100)),
                ('delivery_date', models.DateTimeField()),
                ('asking_price', models.IntegerField()),
                ('driver_evaluation', models.FloatField(null=True)),
                ('client_evaluation', models.FloatField(null=True)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.requests')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.requests')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_info')),
            ],
        ),
    ]
