class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = fecha
        self.hora = hora

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
            clave = clave.strip()
            valor = valor.strip()

            if clave == 'dd':
                dia = int(valor)
                if dia < 1 or dia > 31:
                    print("Error: El día debe estar entre 1 y 31.")
                else:
                    self.fecha = self.fecha[:2] + valor + self.fecha[2:]
            elif clave == 'mm':
                mes = int(valor)
                if mes < 1 or mes > 12:
                    print("Error: El mes debe estar entre 1 y 12.")
                else:
                    self.fecha = self.fecha[:5] + valor + self.fecha[5:]
            elif clave == 'aaaa':
                self.fecha = valor + self.fecha[4:]
            elif clave == 'HH':
                hora = int(valor)
                if hora < 0 or hora > 23:
                    print("Error: La hora debe estar entre 0 y 23.")
                else:
                    self.hora = self.hora[:2] + valor + self.hora[2:]
            elif clave == 'MM':
                minuto = int(valor)
                if minuto < 0 or minuto > 59:
                    print("Error: Los minutos deben estar entre 0 y 59.")
                else:
                    self.hora = self.hora[:5] + valor + self.hora[5:]
            elif clave == 'SS':
                segundo = int(valor)
                if segundo < 0 or segundo > 59:
                    print("Error: Los segundos deben estar entre 0 y 59.")
                else:
                    self.hora = self.hora[:8] + valor + self.hora[8:]
            else:
                print("Error: Parámetro no válido.")
        except ValueError:
            print("Error: Parámetro no válido.")

    def __str__(self):
        return f "{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha('01/01/2022')
fecha_hora.fijarHora('12:30:45')
print(fecha_hora)  # Salida: 01/01/2022 12:30:45

fecha_hora.fijarFechaHora('02/02/2023 18:15:30')
print(fecha_hora)  # Salida: 02/02/2023 18:15:30

fecha_hora.cambiar('dd=31')
fecha_hora.cambiar('mm=12')
fecha_hora.cambiar('aaaa=2024')
fecha_hora.cambiar('HH=23')
fecha_hora.cambiar('MM=59')
fecha_hora.cambiar('SS=59')
print(fecha_hora)  # Salida: 2024/12/31 23:59:59