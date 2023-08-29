class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        partes = fecha.split('/')
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(':')
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split('=')
        tipo_parametro = partes[0].strip()
        valor_parametro = partes[1].strip()

        if tipo_parametro == 'dd':
            dia = int(valor_parametro)
            if 1 <= dia <= 31:
                self.dia = dia
            else:
                print("Error: Valor inválido para el día")
        elif tipo_parametro == 'mm':
            mes = int(valor_parametro)
            if 1 <= mes <= 12:
                self.mes = mes
            else:
                print("Error: Valor inválido para el mes")
        elif tipo_parametro == 'aaaa':
            anio = int(valor_parametro)
            self.anio = anio
        elif tipo_parametro == 'HH':
            hora = int(valor_parametro)
            if 0 <= hora <= 23:
                self.hora = hora
            else:
                print("Error: Valor inválido para la hora")
        elif tipo_parametro == 'MM':
            minuto = int(valor_parametro)
            if 0 <= minuto <= 59:
                self.minuto = minuto
            else:
                print("Error: Valor inválido para el minuto")
        elif tipo_parametro == 'SS':
            segundo = int(valor_parametro)
            if 0 <= segundo <= 59:
                self.segundo = segundo
            else:
                print("Error: Valor inválido para el segundo")
        else:
            print("Error: Tipo de parámetro no reconocido")

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha('15/06/2023')
fecha_hora.fijarHora('12:30:45')
print(fecha_hora)

fecha_hora.fijarFechaHora('02/09/2022 09:15:00')
print(fecha_hora)

fecha_hora.cambiar('dd=40')
fecha_hora.cambiar('mm=20')
fecha_hora.cambiar('aaaa=2025')
fecha_hora.cambiar('HH=25')
fecha_hora.cambiar('MM=70')
fecha_hora.cambiar('SS=90')

print(fecha_hora)

