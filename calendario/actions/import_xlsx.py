import xlrd
from calendario.models import CalendarioFeriadoImport

filename = 'calendario/feriado.xlsx'
def import_xlsx(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    aux = []
    for row in range(1, sheet.nrows):
        ano = sheet.row(row)[0].value
        mes = sheet.row(row)[1].value
        dia = sheet.row(row)[2].value
        descricao = sheet.row(row)[3].value
        feriado = dict(
        ano=ano,
        mes=mes,
        dia=dia,
        descricao=descricao,
        )
    obj = CalendarioFeriadoImport(**feriado)
    aux.append(obj)
    CalendarioFeriadoImport.objects.bulk_create(aux)
