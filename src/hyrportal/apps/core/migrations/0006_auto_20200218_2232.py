# Generated by Django 2.2.8 on 2020-02-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_wooorderitem_id_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('fortnox', 'Fortnox'), ('visma', 'Visma')], max_length=128),
        ),
    ]