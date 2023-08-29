class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        self.dia, self.mes, self.anio = map(int, fecha.split('/'))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split('=')
        if tipo == 'dd':
            dia = int(valor)
            if 1 <= dia <= 31:
                self.dia = dia
            else:
                print('Día inválido.')
        elif tipo == 'mm':
            mes = int(valor)
            if 1 <= mes <= 12:
                self.mes = mes
            else:
                print('Mes inválido.')
        elif tipo == 'aaaa':
            anio = int(valor)
            if anio >= 0:
                self.anio = anio
            else:
                print('Año inválido.')
        elif tipo == 'HH':
            hora = int(valor)
            if 0 <= hora <= 23:
                self.hora = hora
            else:
                print('Hora inválida.')
        elif tipo == 'MM':
            minuto = int(valor)
            if 0 <= minuto <= 59:
                self.minuto = minuto
            else:
                print('Minuto inválido.')
        elif tipo == 'SS':
            segundo = int(valor)
            if 0 <= segundo <= 59:
                self.segundo = segundo
            else:
                print('Segundo inválido.')
        else:
            print('Parámetro inválido.')

    def __str__(self):
        return f'{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'


# Ejemplo de uso:
fecha_hora = FechaHora('28/05/2023', '12:34:56')
print(fecha_hora)  # Salida: 2023/05/28 12:34:56

fecha_hora.cambiar('dd=2')
fecha_hora.cambiar('mm=13')  # Mes inválido.
fecha_hora.cambiar('aaaa=-2023')  # Año inválido.
fecha_hora.cambiar('HH=25')  # Hora inválida.
fecha_hora.cambiar('MM=61')  # Minuto inválido.
fecha_hora.cambiar('SS=45')  # Segundo inválido.

print(fecha_hora)  # Salida: 2023/02/02 12:34:45
