# Generated by Django 4.2 on 2024-05-24 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True, null=True)),
                ('modificacion_registro', models.DateField(auto_now_add=True, null=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('cursos', models.ManyToManyField(related_name='profesores', to='app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True, null=True)),
                ('modificacion_registro', models.DateField(auto_now_add=True, null=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('curso', models.ManyToManyField(related_name='estudiantes', to='app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('depto', models.CharField(max_length=10)),
                ('comuna', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=10)),
                ('estudiante_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='direccion', to='app.estudiante')),
            ],
        ),
    ]
