# Generated by Django 2.2.8 on 2020-03-03 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_fortnoxsettings_freight_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortnoxsettings',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
