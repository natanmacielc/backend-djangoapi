# Generated by Django 3.2.6 on 2021-08-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiscocalendario',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'FiscoCalendario',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='fisco',
            options={'managed': False},
        ),
    ]
