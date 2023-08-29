class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        separador = '/' if '/' in fecha else '-'
        partes = fecha.split(separador)
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(':')
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        partes = parametro.split('=')
        tipo = partes[0].strip()
        valor = int(partes[1].strip())

        if tipo == 'dd':
            if valor < 1 or valor > 31:
                print('Error: El día debe estar entre 1 y 31.')
            else:
                self.dia = valor
        elif tipo == 'mm':
            if valor < 1 or valor > 12:
                print('Error: El mes debe estar entre 1 y 12.')
            else:
                self.mes = valor
        elif tipo == 'aaaa':
            if valor < 0:
                print('Error: El año debe ser un valor positivo.')
            else:
                self.anio = valor
        elif tipo == 'HH':
            if valor < 0 or valor > 23:
                print('Error: La hora debe estar entre 0 y 23.')
            else:
                self.hora = valor
        elif tipo == 'MM':
            if valor < 0 or valor > 59:
                print('Error: Los minutos deben estar entre 0 y 59.')
            else:
                self.minuto = valor
        elif tipo == 'SS':
            if valor < 0 or valor > 59:
                print('Error: Los segundos deben estar entre 0 y 59.')
            else:
                self.segundo = valor
        else:
            print('Error: Tipo de parámetro inválido.')

    def __str__(self):
        fecha = f'{self.anio:04d}/{self.mes:02d}/{self.dia:02d}'
        hora = f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'
        return f'{fecha} {hora}'


# Ejemplo de uso:
fecha_hora = FechaHora()
fecha_hora.fijarFecha('29/06/2023')
fecha_hora.fijarHora('12:30:45')
print(fecha_hora)  # Imprime: 2023/06/29 12:30:45

fecha_hora.fijarFechaHora('01-01-2000 00:00:00')
print(fecha_hora)  # Imprime: 2000/01/01 00:00:00

fecha_hora.cambiar('dd=2')
print(fecha_hora)  # Imprime: 2000/01

