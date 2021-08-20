# Generated by Django 3.2.6 on 2021-08-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('CPF', models.CharField(max_length=20)),
                ('Telefone', models.CharField(max_length=20, null=True)),
                ('Celular', models.CharField(max_length=20, null=True)),
                ('NomeUsuario', models.CharField(max_length=50)),
                ('DataCadastro', models.DateField(auto_now_add=True)),
                ('DataAlteracao', models.DateField(auto_now=True, null=True)),
                ('Ativo', models.BooleanField(default=True, null=True)),
                ('Perfil', models.CharField(max_length=50, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]