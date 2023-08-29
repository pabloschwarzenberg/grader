class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        param, valor = parametro.split('=')

        if param == 'dd':
            if int(valor) < 1 or int(valor) > 31:
                print("Error: El día debe estar entre 1 y 31.")
                return
            self.fecha = self.fecha[:8] + valor + self.fecha[10:]

        elif param == 'mm':
            if int(valor) < 1 or int(valor) > 12:
                print("Error: El mes debe estar entre 1 y 12.")
                return
            self.fecha = self.fecha[:5] + valor + self.fecha[7:]

        elif param == 'aaaa':
            if int(valor) < 1 or int(valor) > 9999:
                print("Error: El año debe estar entre 1 y 9999.")
                return
            self.fecha = valor + self.fecha[4:]

        elif param == 'HH':
            if int(valor) < 0 or int(valor) > 23:
                print("Error: La hora debe estar entre 0 y 23.")
                return
            self.hora = valor + self.hora[2:]

        elif param == 'MM':
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Los minutos deben estar entre 0 y 59.")
                return
            self.hora = self.hora[:3] + valor + self.hora[5:]

        elif param == 'SS':
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Los segundos deben estar entre 0 y 59.")
                return
            self.hora = self.hora[:6] + valor

        else:
            print("Error: Parámetro inválido.")

    def __str__(self):
        return (f"{self.fecha} {self.hora}")



fecha_hora = FechaHora()

fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
hora = input("Ingrese la hora (HH:MM:SS): ")

fecha_hora.fijarFecha(fecha)
fecha_hora.fijarHora(hora)

cambio = input("Ingrese el cambio a realizar: ")
fecha_hora.cambiar(cambio)

print(fecha_hora)