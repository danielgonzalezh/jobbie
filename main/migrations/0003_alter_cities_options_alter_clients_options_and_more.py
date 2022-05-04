# Generated by Django 4.0.3 on 2022-05-03 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_clients_borndate_alter_workeds_borndate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='departaments',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='genders',
            options={'verbose_name': 'Genero', 'verbose_name_plural': 'Generos'},
        ),
        migrations.AlterModelOptions(
            name='neighborhoods',
            options={'verbose_name': 'Barrio', 'verbose_name_plural': 'Barrios'},
        ),
        migrations.AlterModelOptions(
            name='workeds',
            options={'verbose_name': 'Trabajador', 'verbose_name_plural': 'Trabajadores'},
        ),
        migrations.AlterField(
            model_name='cities',
            name='departametId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.departaments', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='bornDate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='gender',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.genders'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='mobile',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='neighborhoodId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.neighborhoods', verbose_name='Barrio'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='photo',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='clientes'),
        ),
        migrations.AlterField(
            model_name='neighborhoods',
            name='cityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.cities', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='workeds',
            name='descripcion_personal',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='workeds',
            name='gender',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.genders'),
        ),
        migrations.AlterField(
            model_name='workeds',
            name='mobile',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='workeds',
            name='neighborhoodId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.neighborhoods', verbose_name='Barrio'),
        ),
        migrations.AlterField(
            model_name='workeds',
            name='photo',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='clientes'),
        ),
    ]
