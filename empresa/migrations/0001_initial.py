# Generated by Django 3.2.6 on 2021-08-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clienteempresa',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ClienteEmpresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=20)),
                ('dataabertura', models.DateTimeField(blank=True, db_column='DataAbertura', null=True)),
                ('bairro', models.CharField(blank=True, db_column='Bairro', max_length=150, null=True)),
                ('municipio', models.CharField(blank=True, db_column='Municipio', max_length=150, null=True)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=2, null=True)),
                ('razaosocial', models.CharField(blank=True, db_column='RazaoSocial', max_length=250, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=150, null=True)),
                ('nomefantasia', models.CharField(blank=True, db_column='NomeFantasia', max_length=250, null=True)),
                ('porte', models.CharField(blank=True, db_column='Porte', max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, db_column='Telefone', max_length=20, null=True)),
                ('telefoneadicional', models.CharField(blank=True, db_column='TelefoneAdicional', max_length=20, null=True)),
                ('situacaocadastral', models.CharField(blank=True, db_column='SituacaoCadastral', max_length=250, null=True)),
                ('datasituacaocadastral', models.DateTimeField(blank=True, db_column='DataSituacaoCadastral', null=True)),
                ('motivosituacaocadastral', models.CharField(blank=True, db_column='MotivoSituacaoCadastral', max_length=500, null=True)),
                ('situacaoespecial', models.CharField(blank=True, db_column='SituacaoEspecial', max_length=250, null=True)),
                ('datasituacaoespecial', models.DateTimeField(blank=True, db_column='DataSituacaoEspecial', null=True)),
                ('atividadeprincipal', models.CharField(blank=True, db_column='AtividadePrincipal', max_length=250, null=True)),
                ('atividadesecundaria', models.CharField(blank=True, db_column='AtividadeSecundaria', max_length=250, null=True)),
                ('endereco', models.CharField(blank=True, db_column='Endereco', max_length=250, null=True)),
                ('numero', models.CharField(blank=True, db_column='Numero', max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, db_column='Complemento', max_length=150, null=True)),
                ('cep', models.CharField(blank=True, db_column='Cep', max_length=10, null=True)),
                ('datacadastro', models.DateTimeField(auto_now_add=True, db_column='DataCadastro')),
                ('dataalteracao', models.DateTimeField(auto_now=True, db_column='DataAlteracao', null=True)),
                ('ativo', models.BooleanField(blank=True, db_column='Ativo', default=True, null=True)),
            ],
            options={
                'db_table': 'Empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresaplanocontas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'EmpresaPlanoContas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=20)),
                ('cnae', models.CharField(blank=True, db_column='CNAE', max_length=20, null=True)),
                ('codigoservico', models.CharField(blank=True, db_column='CodigoServico', max_length=50, null=True)),
                ('descricaoservico', models.CharField(blank=True, db_column='DescricaoServico', max_length=150, null=True)),
                ('tipofornecedor', models.CharField(blank=True, db_column='TipoFornecedor', max_length=50, null=True)),
                ('servicotomado', models.CharField(blank=True, db_column='ServicoTomado', max_length=50, null=True)),
                ('datacadastro', models.DateTimeField(auto_now_add=True, db_column='DataCadastro')),
                ('dataalteracao', models.DateTimeField(auto_now=True, db_column='DataAlteracao', null=True)),
                ('ativo', models.BooleanField(blank=True, db_column='Ativo', default=True, null=True)),
            ],
            options={
                'db_table': 'Fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grupoempresa',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'GrupoEmpresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanocontasEmpresaplanocontas',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('empresaid_id', models.CharField(db_column='EmpresaID_id', max_length=32)),
                ('planocontasreferencialid_id', models.CharField(db_column='PlanoContasReferencialID_id', max_length=32)),
            ],
            options={
                'db_table': 'PlanoContas_empresaplanocontas',
                'managed': False,
            },
        ),
    ]
