# Generated by Django 5.1 on 2024-11-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('act_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('act_nombre', models.CharField(max_length=100)),
                ('act_riesgo', models.CharField(max_length=200)),
                ('act_medida_control', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('pre_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pre_descripcion', models.CharField(max_length=200)),
                ('pre_cargo', models.CharField(max_length=50)),
                ('pre_respuesta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RiesgoCritico',
            fields=[
                ('rc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rc_nombre', models.CharField(max_length=100)),
                ('rc_pregunta', models.CharField(max_length=200)),
                ('rc_respuesta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('art_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('art_trab_simultaneo', models.BooleanField(default=False)),
                ('art_estado_trab', models.BooleanField(default=False)),
                ('art_hora_inicio', models.TimeField()),
                ('art_hora_fin', models.TimeField()),
                ('actividad', models.ManyToManyField(to='art_app.actividad')),
                ('empleado', models.ManyToManyField(to='personal_app.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='riesgo_critico',
            field=models.ManyToManyField(to='art_app.riesgocritico'),
        ),
    ]
