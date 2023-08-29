class FechaHora:
    def __init__(self, fecha='', hora=''):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

        if fecha:
            self.fijarFecha(fecha)

        if hora:
            self.fijarHora(hora)

    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.dia, self.mes, self.anio = fecha.split('/')
        elif '-' in fecha:
            self.dia, self.mes, self.anio = fecha.split('-')

        self.dia = int(self.dia)
        self.mes = int(self.mes)
        self.anio = int(self.anio)

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split('=')

        if tipo == 'dd':
            valor = int(valor)
            if valor < 1 or valor > 31:
                print('Error: El día debe estar entre 1 y 31.')
                return
            self.dia = valor
        elif tipo == 'mm':
            valor = int(valor)
            if valor < 1 or valor > 12:
                print('Error: El mes debe estar entre 1 y 12.')
                return
            self.mes = valor
        elif tipo == 'aaaa':
            valor = int(valor)
            self.anio = valor
        elif tipo == 'HH':
            valor = int(valor)
            if valor < 0 or valor > 23:
                print('Error: La hora debe estar entre 0 y 23.')
                return
            self.hora = valor
        elif tipo == 'MM':
            valor = int(valor)
            if valor < 0 or valor > 59:
                print('Error: El minuto debe estar entre 0 y 59.')
                return
            self.minuto = valor
        elif tipo == 'SS':
            valor = int(valor)
            if valor < 0 or valor > 59:
                print('Error: El segundo debe estar entre 0 y 59.')
                return
            self.segundo = valor
        else:
            print('Error: Tipo de parámetro inválido.')

    def __str__(self):
        fecha = f'{self.anio:04d}/{self.mes:02d}/{self.dia:02d}'
        hora = f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'
        return f'{fecha} {hora}'

if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFechaHora('01/01/2023 12:34:56')
    print(fecha_hora)

    fecha_hora.cambiar('dd=31')
    fecha_hora.cambiar('mm=12')
    fecha_hora.cambiar('aaaa=2024')
    fecha_hora.cambiar('HH=23')
    fecha_hora.cambiar('MM=59')
    fecha_hora.cambiar('SS=59')
    print(fecha_hora)

           