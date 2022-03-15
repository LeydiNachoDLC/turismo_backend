# Generated by Django 4.0.3 on 2022-03-15 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LugarTurismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20, verbose_name='Descripcion')),
                ('lugar', models.CharField(max_length=20, verbose_name='Lugar')),
                ('fecha', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Turismo',
                'verbose_name_plural': 'Lugares Turisticos',
            },
        ),
        migrations.CreateModel(
            name='TipoTransporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Tipo Transporte',
                'verbose_name_plural': 'Tipos Transportes',
            },
        ),
        migrations.CreateModel(
            name='EmpresaTransporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_Empresa', models.CharField(max_length=20, verbose_name='Cod_Empresa')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=20, verbose_name='Direccion')),
                ('Fecha_insc', models.DateField(verbose_name='Fecha')),
                ('tipo_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='turismo.tipotransporte')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas Registradas',
            },
        ),
    ]