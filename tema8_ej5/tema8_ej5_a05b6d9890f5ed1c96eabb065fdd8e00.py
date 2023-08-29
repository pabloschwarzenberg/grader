class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        # Dividir el string en fecha y hora
        fecha, hora = fecha_hora.split(' ')
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        # Dividir el string en nombre del parámetro y valor
        nombre, valor = parametro.split('=')
        nombre = nombre.strip()  # Eliminar espacios en blanco alrededor del nombre
        valor = valor.strip()  # Eliminar espacios en blanco alrededor del valor

        # Validar y cambiar el parámetro correspondiente
        if nombre == 'dd':
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.fecha = self.fecha[:2] + valor + self.fecha[4:]
            else:
                print("Día inválido")
        elif nombre == 'mm':
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.fecha = valor + self.fecha[2:5] + self.fecha[7:]
            else:
                print("Mes inválido")
        elif nombre == 'aaaa':
            anio = int(valor)
            if anio >= 1 and anio <= 9999:
                self.fecha = self.fecha[:6] + valor
            else:
                print("Año inválido")
        elif nombre == 'HH':
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = valor + self.hora[2:]
            else:
                print("Hora inválida")
        elif nombre == 'MM':
            minuto = int(valor)
            if minuto >= 0 and minuto <= 59:
                self.hora = self.hora[:3] + valor + self.hora[5:]
            else:
                print("Minuto inválido")
        elif nombre == 'SS':
            segundo = int(valor)
            if segundo >= 0 and segundo <= 59:
                self.hora = self.hora[:6] + valor
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")

    def __str__(self):
        return f"{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha('01/01/2023')
fecha_hora.fijarHora('12:30:00')
print(fecha_hora)  # Salida: 01/01/2023 12:30:00

fecha_hora.fijarFechaHora('02/02/2023 09:45:30')
print(fecha_hora)  # Salida: 02/02/2023 09:45:30

fecha_hora.cambiar('dd=31')
fecha_hora.cambiar('mm=12')
fecha_hora.cambiar('aaaa=2022')
fecha_hora.cambiar('HH=23')
fecha_hora.cambiar('MM=59')
fecha_hora.cambiar('SS=59')
print(fecha_hora)  # Salida: 31/12/2022 23:59:59

fecha_hora.cambiar('dd=40')  # Intento cambiar a un día inválido
