# Generated by Django 5.1 on 2024-11-06 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_app', '0001_initial'),
        ('personal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='artEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado_art', models.BooleanField(default=False)),
                ('supervisor_asignado', models.CharField(max_length=100)),
                ('art_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_app.art')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_app.empleado')),
            ],
        ),
        migrations.AlterField(
            model_name='art',
            name='empleado',
            field=models.ManyToManyField(related_name='empleados', through='art_app.artEmpleado', to='personal_app.empleado'),
        ),
    ]