class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        fecha_str = fecha_str.replace('-', '/')
        dia, mes, anio = map(int, fecha_str.split('/'))
        self.fecha = (dia, mes, anio)

    def fijarHora(self, hora_str):
        hora, minuto, segundo = map(int, hora_str.split(':'))
        self.hora = (hora, minuto, segundo)

    def fijarFechaHora(self, fechahora_str):
        partes = fechahora_str.split()
        fecha_str = partes[0]
        hora_str = partes[1]
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, cambio_str):
        cambio_str = cambio_str.replace(' ', '')
        parametro, valor = cambio_str.split('=')
        valor = int(valor)
        if parametro == 'dd':
            if 1 <= valor <= 31:
                dia, mes, anio = self.fecha
                self.fecha = (valor, mes, anio)
            else:
                print('Error: el día debe estar entre 1 y 31')
        elif parametro == 'mm':
            if 1 <= valor <= 12:
                dia, mes, anio = self.fecha
                self.fecha = (dia, valor, anio)
            else:
                print('Error: el mes debe estar entre 1 y 12')
        elif parametro == 'aaaa':
            if 1 <= valor <= 9999:
                dia, mes, anio = self.fecha
                self.fecha = (dia, mes, valor)
            else:
                print('Error: el año debe estar entre 1 y 9999')
        elif parametro == 'HH':
            if 0 <= valor <= 23:
                hora, minuto, segundo = self.hora
                self.hora = (valor, minuto, segundo)
            else:
                print('Error: la hora debe estar entre 0 y 23')
        elif parametro == 'MM':
            if 0 <= valor <= 59:
                hora, minuto, segundo = self.hora
                self.hora = (hora, valor, segundo)
            else:
                print('Error: el minuto debe estar entre 0 y 59')
        elif parametro == 'SS':
            if 0 <= valor <= 59:
                hora, minuto, segundo = self.hora
                self.hora = (hora, minuto, valor)
            else:
                print('Error: el segundo debe estar entre 0 y 59')

    def __str__(self):
        dia, mes, anio = self.fecha
        hora, minuto, segundo = self.hora
        return '{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(anio, mes, dia, hora, minuto, segundo)


fecha_hora = FechaHora()
fecha_hora.fijarFechaHora('01/01/2022 12:00:00')
print(fecha_hora)
fecha_hora.cambiar('dd=2')
print(fecha_hora)
fecha_hora.cambiar('mm=3')
print(fecha_hora)
fecha_hora.cambiar('aaaa=2023')
print(fecha_hora)
fecha_hora.cambiar('HH=13')
print(fecha_hora)
fecha_hora.cambiar('MM=30')
print(fecha_hora)
fecha_hora.cambiar('SS=45')
print(fecha_hora)
