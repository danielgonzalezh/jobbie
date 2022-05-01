# Generated by Django 4.0.3 on 2022-05-01 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departament', models.CharField(max_length=80, verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.CharField(max_length=80, verbose_name='Barrio')),
                ('cityId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.cities', verbose_name='CiudadesId')),
            ],
        ),
        migrations.CreateModel(
            name='Workeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=100, verbose_name='Apellido')),
                ('mail', models.CharField(max_length=200, verbose_name='Correo')),
                ('bornDate', models.DateTimeField(blank=True, verbose_name='Fecha de nacimiento')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
                ('photo', models.ImageField(default='null', upload_to='clientes')),
                ('mobile', models.IntegerField(verbose_name='Celular')),
                ('descripcion_personal', models.TextField(verbose_name='Descripcion')),
                ('gender', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.genders')),
                ('neighborhoodId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.neighborhoods', verbose_name='Barrio')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=100, verbose_name='Apellido')),
                ('mail', models.CharField(max_length=200, verbose_name='Correo')),
                ('bornDate', models.DateTimeField(blank=True, verbose_name='Fecha de nacimiento')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
                ('photo', models.ImageField(default='null', upload_to='clientes')),
                ('mobile', models.IntegerField(verbose_name='Celular')),
                ('gender', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.genders')),
                ('neighborhoodId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.neighborhoods', verbose_name='Barrio')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='departametId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.departaments', verbose_name='DepartamentoId'),
        ),
    ]