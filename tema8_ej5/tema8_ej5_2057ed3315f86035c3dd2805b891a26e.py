class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        parametro = parametro.strip()
        if parametro.startswith('dd='):
            dia = int(parametro[3:])
            if dia >= 1 and dia <= 31:
                self.fecha = self.fecha[:3] + str(dia) + self.fecha[5:]
            else:
                print("Día inválido")
        elif parametro.startswith('mm='):
            mes = int(parametro[3:])
            if mes >= 1 and mes <= 12:
                self.fecha = self.fecha[:0] + str(mes) + self.fecha[2:]
            else:
                print("Mes inválido")

elif parametro.startswith('aaaa='):
            anio = int(parametro[5:])
            if anio >= 1 and anio <= 9999:
                self.fecha = self.fecha[:6] + str(anio)
            else:
                print("Año inválido")
        elif parametro.startswith('HH='):
            hora = int(parametro[3:])
            if hora >= 0 and hora <= 23:
                self.hora = self.hora[:0] + str(hora) + self.hora[2:]
            else:
                print("Hora inválida")
        elif parametro.startswith('MM='):
            minutos = int(parametro[3:])
            if minutos >= 0 and minutos <= 59:
                self.hora = self.hora[:3] + str(minutos) + self.hora[5:]
            else:
                print("Minutos inválidos")
        elif parametro.startswith('SS='):
            segundos = int(parametro[3:])
            if segundos >= 0 and segundos <= 59:
                self.hora = self.hora[:6] + str(segundos)
            else:
                print("Segundos inválidos")
        else:
            print("Parámetro inválido")

    def __str__(self):
    return f"{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora("01/01/2023", "12:00:00")
print(fecha_hora)  # Salida: 01/01/2023 12:00:00

fecha_hora.fijarFecha("05/05/2023")
fecha_hora.fijarHora("18:30:45")
print(fecha_hora)  # Salida: 05/05/2023 18:30:45

fecha_hora.fijarFechaHora("10/10/2023 08:15:30")
print(fecha_hora)  # Salida: 10/10/2023 08:15:30

fecha_hora.cambiar("dd=15")
fecha_hora.cambiar("HH=23")
print(fecha_hora)  # Salida: 15/10/2023 23:15:30

fecha_hora.cambiar("dd=40")  # Salida: Día inválido
fecha_hora.cambiar

           