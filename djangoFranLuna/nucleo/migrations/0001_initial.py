# Generated by Django 2.2.5 on 2022-05-10 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('precio', models.FloatField(verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'compra',
                'verbose_name_plural': 'compras',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('receta', models.CharField(choices=[(1, 's'), (2, 'n')], default=1, max_length=1, verbose_name='Receta')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
            ],
            options={
                'verbose_name': 'medicamento',
                'verbose_name_plural': 'medicamentos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('fechaAlta', models.IntegerField(verbose_name='Fecha de alta')),
                ('especialidad', models.CharField(choices=[(1, 'familia'), (2, 'digestivo'), (3, 'neurologia'), (4, 'dematologia'), (5, 'traumatologia')], max_length=40, verbose_name='Especialidad')),
                ('usuario', models.CharField(max_length=30, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'medico',
                'verbose_name_plural': 'medicos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('foto', models.ImageField(unique=True, upload_to='fotos/pacientes/', verbose_name='Foto')),
                ('activo', models.BooleanField(default=False)),
                ('usuario', models.CharField(max_length=30, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CompraMedicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Compra', verbose_name='Compra')),
                ('idMedicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Medicamento', verbose_name='Medicamento')),
            ],
            options={
                'verbose_name': 'compramedicamento',
                'verbose_name_plural': 'compramedicamentos',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='idPaciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Paciente', verbose_name='Paciente'),
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('idMedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Medico', verbose_name='Médico')),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'cita',
                'verbose_name_plural': 'citas',
                'ordering': ['-id'],
            },
        ),
    ]
