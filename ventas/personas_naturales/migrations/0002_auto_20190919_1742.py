# Generated by Django 2.2.5 on 2019-09-19 22:42

from django.db import migrations, models
import ventas.validaciones


class Migration(migrations.Migration):

    dependencies = [
        ('personas_naturales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona_natural',
            name='apellidos',
            field=models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras]),
        ),
        migrations.AlterField(
            model_name='persona_natural',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[ventas.validaciones.validate_cedula], verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='persona_natural',
            name='celular',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular]),
        ),
        migrations.AlterField(
            model_name='persona_natural',
            name='nombres',
            field=models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras]),
        ),
        migrations.AlterField(
            model_name='persona_natural',
            name='tel_domicilio',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_fono_convencional], verbose_name='Teléfono Domicilio'),
        ),
        migrations.AlterField(
            model_name='persona_natural',
            name='tel_trabajo',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[ventas.validaciones.validate_fono_convencional], verbose_name='Teléfono Trabajo'),
        ),
    ]