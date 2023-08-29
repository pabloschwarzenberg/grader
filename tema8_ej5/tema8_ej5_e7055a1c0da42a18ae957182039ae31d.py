class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        try:
            clave, valor = parametro.split('=')
            if clave == 'dd':
                dia = int(valor)
                if 1 <= dia <= 31:
                    self.fecha = self.fecha[:8] + str(dia)
                else:
                    print("Error: el día ingresado es inválido.")
            elif clave == 'mm':
                mes = int(valor)
                if 1 <= mes <= 12:
                    self.fecha = self.fecha[:5] + str(mes).zfill(2) + self.fecha[7:]
                else:
                    print("Error: el mes ingresado es inválido.")
            elif clave == 'aaaa':
                anio = int(valor)
                if 1900 <= anio <= 9999:
                    self.fecha = str(anio) + self.fecha[4:]
                else:
                    print("Error: el año ingresado es inválido.")
            elif clave == 'HH':
                hora = int(valor)
                if 0 <= hora <= 23:
                    self.hora = str(hora).zfill(2) + self.hora[2:]
                else:
                    print("Error: la hora ingresada es inválida.")
            elif clave == 'MM':
                minutos = int(valor)
                if 0 <= minutos <= 59:
                    self.hora = self.hora[:3] + str(minutos).zfill(2) + self.hora[5:]
                else:
                    print("Error: los minutos ingresados son inválidos.")
            elif clave == 'SS':
                segundos = int(valor)
                if 0 <= segundos <= 59:
                    self.hora = self.hora[:6] + str(segundos).zfill(2)
                else:
                    print("Error: los segundos ingresados son inválidos.")
            else:
                print("Error: el parámetro ingresado no es válido.")
        except ValueError:
            print("Error: formato de parámetro incorrecto.")

    def __str__(self):
        return f"{self.fecha} {self.hora}"

# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha("15/06/2023")
fecha_hora.fijarHora("12:30:00")
print(fecha_hora)  # Imprime "15/06/2023 12:30:00"

fecha_hora.fijarFechaHora("20/07/2023 10:45:00")
print(fecha_hora)  # Imprime "20/07/2023 10:45:00"

fecha_hora.cambiar("dd=25")
fecha_hora.cambiar("mm=11")
fecha_hora.cambiar("aaaa=2022")
fecha_hora.cambiar("HH=23")
fecha_hora.cambiar("MM=59")
fecha_hora.cambiar("SS=45")
print(fecha_hora)  # Imprime "2022/11/25 23:59:45"

fecha_hora.cambiar("dd=40")