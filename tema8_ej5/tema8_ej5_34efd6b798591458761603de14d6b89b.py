from datetime import datetime

class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        if self.fecha and self.hora:
            return self.fecha.strftime('%Y/%m/%d') + ' ' + self.hora.strftime('%H:%M:%S')
        else:
            return ""

    def fijarFecha(self, fecha):
        try:
            self.fecha = datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            try:
                self.fecha = datetime.strptime(fecha, '%d-%m-%Y')
            except ValueError:
                print('Formato de fecha incorrecto')

    def fijarHora(self, hora):
        try:
            self.hora = datetime.strptime(hora, '%H:%M:%S')
        except ValueError:
            print('Formato de hora incorrecto')

    def fijarFechaHora(self, fechahora):
        try:
            fecha_hora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M:%S')
            self.fecha = fecha_hora
            self.hora = fecha_hora
        except ValueError:
            try:
                fecha_hora = datetime.strptime(fechahora, '%d-%m-%Y %H:%M:%S')
                self.fecha = fecha_hora
                self.hora = fecha_hora
            except ValueError:
                print('Formato de fecha y hora incorrecto')

    def cambiar(self, parte):
        parte = parte.replace(' ', '')
        if '=' in parte:
            parametro, valor = parte.split('=')
            if parametro == 'dd':
                if 1 <= int(valor) <= 31:
                    self.fecha = self.fecha.replace(day=int(valor))
                else:
                    print('Día inválido')
            elif parametro == 'mm':
                if 1 <= int(valor) <= 12:
                    self.fecha = self.fecha.replace(month=int(valor))
                else:
                    print('Mes inválido')
            elif parametro == 'aaaa':
                if int(valor) >= 1:
                    self.fecha = self.fecha.replace(year=int(valor))
                else:
                    print('Año inválido')
            elif parametro == 'HH':
                if 0 <= int(valor) <= 23:
                    self.hora = self.hora.replace(hour=int(valor))
                else:
                    print('Hora inválida')
            elif parametro == 'MM':
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(minute=int(valor))
                else:
                    print('Minuto inválido')
            elif parametro == 'SS':
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(second=int(valor))
                else:
                    print('Segundo inválido')
            else:
                print('Parámetro desconocido')
        else:
            print('Formato de cambio incorrecto')

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    fh
