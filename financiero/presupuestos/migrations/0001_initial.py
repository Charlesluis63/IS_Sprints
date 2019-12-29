# Generated by Django 2.2.4 on 2019-12-28 18:44

from django.db import migrations, models
import django.db.models.deletion
import financiero.validaciones


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas_juridicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioAportacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
                ('porcentaje_facultades', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioHospedajeAlimentacionDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioHospedajeAlimentacionPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioInstalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_con_iva', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioOtroSuministro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioPlantillaDelPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioPrecio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioProspecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioPublicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioServicioAereo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TarifarioServicioAlimentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incluye_iva', models.BooleanField(default=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo])),
                ('version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarifario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(blank=True, null=True)),
                ('aportaciones', models.ManyToManyField(to='presupuestos.TarifarioAportacion')),
                ('docente', models.ManyToManyField(to='presupuestos.TarifarioDocente')),
                ('hospedaje_alimentacion_docente', models.ManyToManyField(to='presupuestos.TarifarioHospedajeAlimentacionDocente', verbose_name='Hospedaje y alimentación docente')),
                ('hospedaje_alimentacion_personal', models.ManyToManyField(to='presupuestos.TarifarioHospedajeAlimentacionPersonal', verbose_name='Hospedaje y alimentación personal ejecución')),
                ('instalaciones', models.ManyToManyField(to='presupuestos.TarifarioInstalacion')),
                ('materiales_del_evento', models.ManyToManyField(to='presupuestos.TarifarioMaterial')),
                ('otros_suministros', models.ManyToManyField(to='presupuestos.TarifarioOtroSuministro')),
                ('plantilla_del_personal', models.ManyToManyField(to='presupuestos.TarifarioPlantillaDelPersonal')),
                ('precios', models.ManyToManyField(to='presupuestos.TarifarioPrecio')),
                ('productos', models.ManyToManyField(to='presupuestos.TarifarioProducto')),
                ('prospecto', models.ManyToManyField(to='presupuestos.TarifarioProspecto')),
                ('publicidad', models.ManyToManyField(to='presupuestos.TarifarioPublicidad')),
                ('servicio_de_alimentacion', models.ManyToManyField(to='presupuestos.TarifarioServicioAlimentacion', verbose_name='Servicio de alimentación')),
                ('servicios_aereos', models.ManyToManyField(to='presupuestos.TarifarioServicioAereo', verbose_name='Servicios Aéreos')),
            ],
        ),
        migrations.CreateModel(
            name='PresupuestoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingresar nombre de evento', max_length=200, verbose_name='Nombre de Evento')),
                ('codigo', models.CharField(max_length=200, verbose_name='Código')),
                ('nombre_instructor', models.CharField(max_length=200, verbose_name='Nombre del instructor')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('horario', models.CharField(blank=True, max_length=200, null=True)),
                ('n_horas', models.IntegerField(validators=[financiero.validaciones.validate_positivo], verbose_name='No. Horas')),
                ('costo_hora_instructor', models.DecimalField(decimal_places=3, max_digits=7, validators=[financiero.validaciones.validate_positivo], verbose_name='Costo Hora Instructor')),
                ('n_dias', models.IntegerField(validators=[financiero.validaciones.validate_positivo], verbose_name='No. Dias')),
                ('n_participantes', models.IntegerField(blank=True, null=True, validators=[financiero.validaciones.validate_positivo], verbose_name='No. Participantes')),
                ('ingresos', models.DecimalField(decimal_places=3, max_digits=14, validators=[financiero.validaciones.validate_positivo], verbose_name='Ingresos sin descuento')),
                ('honorario_instructor', models.DecimalField(decimal_places=3, max_digits=7, validators=[financiero.validaciones.validate_positivo], verbose_name='Honorario Instructor')),
                ('movilizacion_personal', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo], verbose_name='Movilización del personal')),
                ('lapiz', models.BooleanField(default=False)),
                ('pendrives', models.BooleanField(default=False)),
                ('otros_materiales', models.BooleanField(default=False)),
                ('movilizacion_personal_ciudad', models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.validaciones.validate_positivo], verbose_name='Movilización del personal (dentro de la ciudad')),
                ('estado', models.BooleanField(blank=True, default=None, null=True)),
                ('aula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='presupuestos.Aula', verbose_name='Aula')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.Juridica', verbose_name='Empresa')),
                ('modalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='presupuestos.Modalidad', verbose_name='Modalidad')),
            ],
        ),
    ]
