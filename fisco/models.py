from django.db import models
from calendario.models import Calendario

# Create your models here.
class Fisco(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  
    municipio = models.CharField(db_column='Municipio', max_length=150, blank=True, null=True)  
    vencimento = models.DateTimeField(db_column='Vencimento', blank=True, null=True)  
    regratributo = models.CharField(db_column='RegraTributo', max_length=20, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'Fisco'


class Fiscocalendario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    fiscoid = models.ForeignKey(Fisco, on_delete=models.CASCADE, db_column='FiscoID')  
    calendarioid = models.ForeignKey(Calendario, on_delete=models.CASCADE, db_column='CalendarioID')  

    class Meta:
        managed = False
        db_table = 'FiscoCalendario'





