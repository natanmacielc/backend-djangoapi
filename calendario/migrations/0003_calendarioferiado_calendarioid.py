# Generated by Django 3.2.6 on 2021-08-20 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_auto_20210820_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarioferiado',
            name='calendarioid',
            field=models.ForeignKey(db_column='CalendarioID', default='', on_delete=django.db.models.deletion.CASCADE, to='calendario.calendario'),
            preserve_default=False,
        ),
    ]
