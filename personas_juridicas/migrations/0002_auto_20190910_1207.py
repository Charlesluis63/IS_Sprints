# Generated by Django 2.2.4 on 2019-09-10 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas_juridicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Sector')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Tipo de Empresa')),
            ],
        ),
        migrations.AlterField(
            model_name='juridica',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.Sector'),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='tipo_empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_juridicas.TipoEmpresa'),
        ),
    ]