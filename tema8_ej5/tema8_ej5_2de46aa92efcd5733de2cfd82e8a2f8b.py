class FechaHora:
    def __init__(self):
        self.fecha = "01/01/0000"
        self.hora = "00:00:00"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(" ")
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        key, value = parametro.split("=")

        if key == "dd":
            dia = int(value)
            if 1 <= dia <= 31:
                self.fecha = self.fecha[:3] + value + self.fecha[5:]
            else:
                print("Error: Valor de día inválido.")
        elif key == "mm":
            mes = int(value)
            if 1 <= mes <= 12:
                self.fecha = self.fecha[:0] + value + self.fecha[2:]
            else:
                print("Error: Valor de mes inválido.")
        elif key == "aaaa":
            if len(value) == 4:
                self.fecha = value + self.fecha[4:]
            else:
                print("Error: Valor de año inválido.")
        elif key == "HH":
            hora = int(value)
            if 0 <= hora <= 23:
                self.hora = value + self.hora[2:]
            else:
                print("Error: Valor de hora inválido.")
        elif key == "MM":
            minuto = int(value)
            if 0 <= minuto <= 59:
                self.hora = self.hora[:0] + value + self.hora[2:]
            else:
                print("Error: Valor de minuto inválido.")
        elif key == "SS":
            segundo = int(value)
            if 0 <= segundo <= 59:
                self.hora = self.hora[:3] + value
            else:
                print("Error: Valor de segundo inválido.")
        else:
            print("Error: Parámetro no válido.")

    def __str__(self):
        return f"{self.fecha} {self.hora}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    print(fecha_hora)

    fecha_hora.fijarFecha("31/12/2022")
    fecha_hora.fijarHora("23:59:59")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("01/01/2023 00:00:01")
    print(fecha_hora)

    fecha_hora.cambiar("dd=2")
    fecha_hora.cambiar("mm=6")
    fecha_hora.cambiar("aaaa=2023")
    fecha_hora.cambiar("HH=10")
    fecha_hora.cambiar("MM=30")
    fecha_hora.cambiar("SS=45")
    fecha_hora.cambiar("dd=40")
    print(fecha_hora)

           