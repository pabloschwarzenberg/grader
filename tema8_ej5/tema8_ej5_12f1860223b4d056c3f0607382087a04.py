import re
from datetime import datetime

class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        fecha_str = re.sub(r'[-/]', '', fecha_str)
        try:
            self.fecha = datetime.strptime(fecha_str, '%d%m%Y').date()
        except ValueError:
            print('Formato de fecha incorrecto. Usa dd/mm/aaaa o dd-mm-aaaa')

    def fijarHora(self, hora_str):
        hora_str = re.sub(r'[:]', '', hora_str)
        try:
            self.hora = datetime.strptime(hora_str, '%H%M%S').time()
        except ValueError:
            print('Formato de hora incorrecto. Usa HH:MM:SS')

    def fijarFechaHora(self, fechahora_str):
        fechahora_str = re.sub(r'[-/: ]', '', fechahora_str)
        try:
            fechahora = datetime.strptime(fechahora_str, '%d%m%Y%H%M%S')
            self.fecha = fechahora.date()
            self.hora = fechahora.time()
        except ValueError:
            print('Formato de fecha y hora incorrecto. Usa dd/mm/aaaa HH:MM:SS')

    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        if '=' not in parametro:
            print('Formato de parámetro incorrecto. Usa tipo=valor')
            return

        tipo, valor = parametro.split('=')
        if tipo == 'dd':
            if not valor.isdigit() or int(valor) < 1 or int(valor) > 31:
                print('Valor de día incorrecto')
                return
            self.fecha = self.fecha.replace(day=int(valor))
        elif tipo == 'mm':
            if not valor.isdigit() or int(valor) < 1 or int(valor) > 12:
                print('Valor de mes incorrecto')
                return
            self.fecha = self.fecha.replace(month=int(valor))
        elif tipo == 'aaaa':
            if not valor.isdigit() or int(valor) < 1:
                print('Valor de año incorrecto')
                return
            self.fecha = self.fecha.replace(year=int(valor))
        elif tipo == 'HH':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 23:
                print('Valor de hora incorrecto')
                return
            self.hora = self.hora.replace(hour=int(valor))
        elif tipo == 'MM':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 59:
                print('Valor de minuto incorrecto')
                return
            self.hora = self.hora.replace(minute=int(valor))
        elif tipo == 'SS':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 59:
                print('Valor de segundo incorrecto')
                return
            self.hora = self.hora.replace(second=int(valor))
        else:
            print('Tipo de parámetro desconocido:', tipo)

    def __str__(self):
        fecha_str = self.fecha.strftime('%Y/%m/%d')
        hora_str = self.hora.strftime('%H:%M:%S')
        return fecha_str + ' ' + hora_str

