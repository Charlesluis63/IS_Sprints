# Generated by Django 2.2.5 on 2019-09-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte_contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportecontacto',
            name='correo_electronico',
            field=models.EmailField(max_length=100),
        ),
    ]
