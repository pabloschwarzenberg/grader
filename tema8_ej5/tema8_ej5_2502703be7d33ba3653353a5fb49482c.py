import datetime

class FechaHora:
    def __init__(self):
        self.fecha_hora = datetime.datetime.now()

    def fijarFecha(self, fecha):
        try:
            self.fecha_hora = datetime.datetime.strptime(fecha, '%d/%m/%Y').replace(hour=self.fecha_hora.hour, minute=self.fecha_hora.minute, second=self.fecha_hora.second)
        except ValueError:
            try:
                self.fecha_hora = datetime.datetime.strptime(fecha, '%d-%m-%Y').replace(hour=self.fecha_hora.hour, minute=self.fecha_hora.minute, second=self.fecha_hora.second)
            except ValueError:
                print('Formato de fecha no válido')

    def fijarHora(self, hora):
        try:
            temp = datetime.datetime.strptime(hora, '%H:%M:%S')
            self.fecha_hora = self.fecha_hora.replace(hour=temp.hour, minute=temp.minute, second=temp.second)
        except ValueError:
            print('Formato de hora no válido')

    def fijarFechaHora(self, fecha_hora):
        try:
            self.fecha_hora = datetime.datetime.strptime(fecha_hora, '%d/%m/%Y %H:%M:%S')
        except ValueError:
            try:
                self.fecha_hora = datetime.datetime.strptime(fecha_hora, '%d-%m-%Y %H:%M:%S')
            except ValueError:
                print('Formato de fecha y hora no válido')

    def cambiar(self, parametro):
        try:
            tipo, valor = parametro.replace(" ", "").split('=')
            if tipo.lower() == 'dd':
                if 1 <= int(valor) <= 31:
                    self.fecha_hora = self.fecha_hora.replace(day=int(valor))
                else:
                    print('Día no válido')
            elif tipo.lower() == 'mm':
                if 1 <= int(valor) <= 12:
                    self.fecha_hora = self.fecha_hora.replace(month=int(valor))
                else:
                    print('Mes no válido')
            elif tipo.lower() == 'aaaa':
                self.fecha_hora = self.fecha_hora.replace(year=int(valor))
            elif tipo.lower() == 'hh':
                if 0 <= int(valor) <= 23:
                    self.fecha_hora = self.fecha_hora.replace(hour=int(valor))
                else:
                    print('Hora no válida')
            elif tipo.lower() == 'mi':
                if 0 <= int(valor) <= 59:
                    self.fecha_hora = self.fecha_hora.replace(minute=int(valor))
                else:
                    print('Minuto no válido')
            elif tipo.lower() == 'ss':
                if 0 <= int(valor) <= 59:
                    self.fecha_hora = self.fecha_hora.replace(second=int(valor))
                else:
                    print('Segundo no válido')
            else:
                print('Parámetro no válido')
        except Exception as e:
            print('Error al cambiar parámetro:', e)

    def __str__(self):
        return self.fecha_hora.strftime('%Y/%m/%d %H:%M:%S')
