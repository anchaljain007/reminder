# Generated by Django 3.0.8 on 2020-07-23 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_no', models.CharField(max_length=100)),
                ('gst', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('repassword', models.CharField(max_length=100)),
            ],
        ),
    ]