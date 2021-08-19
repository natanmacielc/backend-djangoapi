# Generated by Django 3.2.6 on 2021-08-19 01:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fisco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=2)),
                ('municipio', models.CharField(max_length=150)),
                ('vencimento', models.DateField()),
                ('regraTributo', models.IntegerField(choices=[(0, 'Próximo dia útil'), (1, 'Dia útil anterior')])),
                ('dataCadastro', models.DateField(auto_now_add=True)),
                ('dataAlteracao', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nome', 'estado', 'municipio', 'vencimento', 'regraTributo', 'dataCadastro', 'dataAlteracao', 'ativo'],
            },
        ),
    ]
