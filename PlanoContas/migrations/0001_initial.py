# Generated by Django 3.2.6 on 2021-08-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanocontasPlanocontasreferencial',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Codigo', max_length=50)),
                ('descricao', models.CharField(db_column='Descricao', max_length=150)),
                ('datacadastro', models.DateTimeField(auto_now_add=True, db_column='DataCadastro')),
                ('dataalteracao', models.DateTimeField(auto_now=True, db_column='DataAlteracao', null=True)),
                ('ativo', models.BooleanField(db_column='Ativo', default=True)),
            ],
            options={
                'db_table': 'PlanoContas_planocontasreferencial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planocontasreferencial',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Codigo', max_length=50)),
                ('descricao', models.CharField(db_column='Descricao', max_length=150)),
                ('datacadastro', models.DateTimeField(db_column='DataCadastro')),
                ('dataalteracao', models.DateTimeField(blank=True, db_column='DataAlteracao', null=True)),
                ('ativo', models.BooleanField(blank=True, db_column='Ativo', null=True)),
            ],
            options={
                'db_table': 'PlanoContasReferencial',
                'managed': False,
            },
        ),
    ]
