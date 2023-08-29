class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        fecha_parts = fecha.split('/')
        self.dia = int(fecha_parts[0])
        self.mes = int(fecha_parts[1])
        self.anio = int(fecha_parts[2])

    def fijarHora(self, hora):
        hora_parts = hora.split(':')
        self.hora = int(hora_parts[0])
        self.minuto = int(hora_parts[1])
        self.segundo = int(hora_parts[2])

    def fijarFechaHora(self, fecha_hora):
        fecha_hora_parts = fecha_hora.split(' ')
        fecha = fecha_hora_parts[0]
        hora = fecha_hora_parts[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        param_parts = parametro.split('=')
        param_name = param_parts[0].strip()
        param_value = param_parts[1].strip()

        if param_name == 'dd':
            dia = int(param_value)
            if dia >= 1 and dia <= 31:
                self.dia = dia
            else:
                print("Día inválido.")
        elif param_name == 'mm':
            mes = int(param_value)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                print("Mes inválido.")
        elif param_name == 'aaaa':
            anio = int(param_value)
            self.anio = anio
        elif param_name == 'HH':
            hora = int(param_value)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print("Hora inválida.")
        elif param_name == 'MM':
            minuto = int(param_value)
            if minuto >= 0 and minuto <= 59:
                self.minuto = minuto
            else:
                print("Minuto inválido.")
        elif param_name == 'SS':
            segundo = int(param_value)
            if segundo >= 0 and segundo <= 59:
                self.segundo = segundo
            else:
                print("Segundo inválido.")
        else:
            print("Parámetro inválido.")

    def __str__(self):
        fecha = f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d}"
        hora = f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        return f"{fecha} {hora}"


# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha('10/06/2023')
fecha_hora.fijarHora('12:30:45')

print(fecha_hora)  # Salida: 2023/06/10 12:30:45

fecha_hora.cambiar('dd=15')
fecha_hora.cambiar('HH=23')
fecha_hora.cambiar('MM=59')
fecha_hora.cambiar('SS=75')  # Segundo inválido

print(fecha_hora)  # Salida: 2023/06/15 23:59:45
