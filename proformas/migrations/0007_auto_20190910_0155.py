# Generated by Django 2.2.4 on 2019-09-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proformas', '0006_auto_20190910_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proforma',
            name='empresa',
            field=models.CharField(max_length=20),
        ),
    ]