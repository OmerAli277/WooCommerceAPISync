# Generated by Django 2.2.8 on 2020-02-18 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200219_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortnoxapidetails',
            name='access_token',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='fortnoxapidetails',
            name='authorization_Code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='fortnoxapidetails',
            name='client_secret',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='fortnoxapidetails',
            name='seller_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
