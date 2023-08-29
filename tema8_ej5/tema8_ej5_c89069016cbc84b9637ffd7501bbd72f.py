class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2021
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('-'))
        else:
            print('Formato de fecha inválido. Utilice dd/mm/aaaa o dd-mm-aaaa.')

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        clave, valor = parametro.split('=')
        clave = clave.strip()
        valor = valor.strip()

        if clave == 'dd':
            nuevo_dia = int(valor)
            if 1 <= nuevo_dia <= 31:
                self.dia = nuevo_dia
            else:
                print('Día inválido.')
        elif clave == 'mm':
            nuevo_mes = int(valor)
            if 1 <= nuevo_mes <= 12:
                self.mes = nuevo_mes
            else:
                print('Mes inválido.')
        elif clave == 'aaaa':
            nuevo_anio = int(valor)
            if nuevo_anio >= 0:
                self.anio = nuevo_anio
            else:
                print('Año inválido.')
        elif clave == 'HH':
            nueva_hora = int(valor)
            if 0 <= nueva_hora <= 23:
                self.hora = nueva_hora
            else:
                print('Hora inválida.')
        elif clave == 'MM':
            nuevo_minuto = int(valor)
            if 0 <= nuevo_minuto <= 59:
                self.minuto = nuevo_minuto
            else:
                print('Minuto inválido.')
        elif clave == 'SS':
            nuevo_segundo = int(valor)
            if 0 <= nuevo_segundo <= 59:
                self.segundo = nuevo_segundo
            else:
                print('Segundo inválido.')
        else:
            print('Parámetro inválido.')

    def __str__(self):
        return f'{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'


# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha('28/05/2023')
fecha_hora.fijarHora('12:30:00')
print(fecha_hora)  # Salida: 2023/05/28 12:30:00

fecha_hora.fijarFechaHora('30/12/2022 23:59:59')
print(fecha_hora)  # Salida: 2022/12/30 23:59:59

fecha_hora.cambiar('dd=31')
print(fecha_hora)  # Salida: 2022/12/31 23:59:59

fecha_hora.cambiar('mm=13')  # Salida: Mes inválido.
fecha_hora.cambiar('dd=40')  # Salida: Día inválido.
