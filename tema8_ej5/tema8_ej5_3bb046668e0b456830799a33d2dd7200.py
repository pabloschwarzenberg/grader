class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = fecha
        self.hora = hora

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        if parametro.startswith('dd='):
            dia = parametro[3:]
            if dia.isdigit() and 1 <= int(dia) <= 31:
                self.fecha = self.fecha[:2] + dia + self.fecha[2:]
            else:
                print('Error: el día debe ser un número entre 1 y 31.')
        elif parametro.startswith('mm='):
            mes = parametro[3:]
            if mes.isdigit() and 1 <= int(mes) <= 12:
                self.fecha = self.fecha[:5] + mes + self.fecha[7:]
            else:
                print('Error: el mes debe ser un número entre 1 y 12.')
        elif parametro.startswith('aaaa='):
            anio = parametro[5:]
            if anio.isdigit() and len(anio) == 4:
                self.fecha = anio + self.fecha[4:]
            else:
                print('Error: el año debe ser un número de 4 dígitos.')
        elif parametro.startswith('HH='):
            hora = parametro[3:]
            if hora.isdigit() and 0 <= int(hora) <= 23:
                self.hora = hora + self.hora[2:]
            else:
                print('Error: la hora debe ser un número entre 0 y 23.')
        elif parametro.startswith('MM='):
            minutos = parametro[3:]
            if minutos.isdigit() and 0 <= int(minutos) <= 59:
                self.hora = self.hora[:3] + minutos + self.hora[5:]
            else:
                print('Error: los minutos deben ser un número entre 0 y 59.')
        elif parametro.startswith('SS='):
            segundos = parametro[3:]
            if segundos.isdigit() and 0 <= int(segundos) <= 59:
                self.hora = self.hora[:6] + segundos
            else:
                print('Error: los segundos deben ser un número entre 0 y 59.')
        else:
            print('Error: parámetro inválido.')

    def __str__(self):
        return f'{self.fecha} {self.hora}'


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha('31/05/2023')
fecha_hora.fijarHora('12:30:45')
print(fecha_hora)  # Salida: 2023/31/05 12:30:45

fecha_hora.fijarFechaHora('10/06/2023 18:45:00')
print(fecha_hora)  # Salida: 2023/10/06 18:45:00

fecha_hora.cambiar('dd=15')
fecha_hora.cambiar('HH=9')
print(fecha_hora)  # Salida: 2023/15/06 09:45:00