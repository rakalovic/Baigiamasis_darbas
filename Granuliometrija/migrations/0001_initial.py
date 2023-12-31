# Generated by Django 4.2.2 on 2023-06-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projektas',
            fields=[
                ('projekto_id', models.AutoField(primary_key=True, serialize=False)),
                ('projekto_pavadinimas', models.CharField(max_length=500)),
                ('tyrimo_protokolo_numeris', models.CharField(max_length=6)),
                ('grezinio_nr', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Duomenys',
            fields=[
                ('duomenu_id', models.AutoField(primary_key=True, serialize=False)),
                ('pries_praplovima', models.DecimalField(decimal_places=2, max_digits=6)),
                ('po_praplovimo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_8_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_4_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_2_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_1_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_0500_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_0250_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_0125_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_0063_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sietas_0_mm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('projektas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Granuliometrija.projektas')),
            ],
        ),
    ]
