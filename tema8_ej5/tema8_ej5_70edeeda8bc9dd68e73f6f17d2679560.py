from datetime import datetime

class FechaHora:
    def __init__(self):
        self.fecha_hora = datetime.now()

    def fijarFecha(self, fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
        self.fecha_hora = self.fecha_hora.replace(year=fecha.year, month=fecha.month, day=fecha.day)

    def fijarHora(self, hora_str):
        hora, minuto, segundo = map(int, hora_str.split(':'))
        self.fecha_hora = self.fecha_hora.replace(hour=hora, minute=minuto, second=segundo)

    def fijarFechaHora(self, fecha_hora_str):
        try:
            self.fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            self.fecha_hora = datetime.strptime(fecha_hora_str, "%d-%m-%Y %H:%M:%S")

    def cambiar(self, parametro):
        tipo, valor = parametro.split('=')
        valor = int(valor)

        if tipo.strip() == 'dd':
            if 1 <= valor <= 31:
                self.fecha_hora = self.fecha_hora.replace(day=valor)
            else:
                print('Día inválido.')
        elif tipo.strip() == 'mm':
            if 1 <= valor <= 12:
                self.fecha_hora = self.fecha_hora.replace(month=valor)
            else:
                print('Mes inválido.')
        elif tipo.strip() == 'aaaa':
            self.fecha_hora = self.fecha_hora.replace(year=valor)
        elif tipo.strip() == 'HH':
            if 0 <= valor <= 23:
                self.fecha_hora = self.fecha_hora.replace(hour=valor)
            else:
                print('Hora inválida.')
        elif tipo.strip() == 'MM':
            if 0 <= valor <= 59:
                self.fecha_hora = self.fecha_hora.replace(minute=valor)
            else:
                print('Minuto inválido.')
        elif tipo.strip() == 'SS':
            if 0 <= valor <= 59:
                self.fecha_hora = self.fecha_hora.replace(second=valor)
            else:
                print('Segundo inválido.')
        else:
            print('Parámetro desconocido.')

    def __str__(self):
        return self.fecha_hora.strftime('%Y/%m/%d %H:%M:%S')

if __name__ == "__main__":
    f = FechaHora()
    f.fijarFecha('31/12/2023')
    f.fijarHora('23:59:59')
    print(str(f))
    f.cambiar('dd=1')
    print(str(f))
    f.cambiar('mm=2')
    print(str(f))
    f.cambiar('aaaa=2022')
    print(str(f))
    f.cambiar('HH=0')
    print(str(f))
    f.cambiar('MM=0')
    print(str(f))
    f.cambiar('SS=0')
    print(str(f))
