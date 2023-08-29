class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        self.fecha, self.hora = fecha_hora.split()

    def cambiar(self, parametro):
        if parametro.startswith("dd="):
            dia = int(parametro.split("=")[1])
            if 1 <= dia <= 31:
                self.fecha = self.fecha[:3] + str(dia) + self.fecha[5:]
            else:
                print("Día inválido")
        elif parametro.startswith("mm="):
            mes = int(parametro.split("=")[1])
            if 1 <= mes <= 12:
                self.fecha = self.fecha[:0] + str(mes).zfill(2) + self.fecha[3:]
            else:
                print("Mes inválido")
        elif parametro.startswith("aaaa="):
            anio = int(parametro.split("=")[1])
            self.fecha = self.fecha[:6] + str(anio) + self.fecha[10:]
        elif parametro.startswith("HH="):
            hora = int(parametro.split("=")[1])
            if 0 <= hora <= 23:
                self.hora = self.hora[:0] + str(hora).zfill(2) + self.hora[2:]
            else:
                print("Hora inválida")
        elif parametro.startswith("MM="):
            minuto = int(parametro.split("=")[1])
            if 0 <= minuto <= 59:
                self.hora = self.hora[:3] + str(minuto).zfill(2) + self.hora[5:]
            else:
                print("Minuto inválido")
        elif parametro.startswith("SS="):
            segundo = int(parametro.split("=")[1])
            if 0 <= segundo <= 59:
                self.hora = self.hora[:6] + str(segundo).zfill(2)
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")

    def __repr__(self):
        return f"{self.fecha} {self.hora}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("01/01/2022")
    fecha_hora.fijarHora("12:00:00")
    print(fecha_hora)

    fecha_hora.fijarFecha("02-02-2023")
    fecha_hora.fijarHora("18:30:45")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("03/03/2024 10:15:30")
    print(fecha_hora)

    fecha_hora.cambiar("dd=10")
    fecha_hora.cambiar("mm=04")
    fecha_hora.cambiar("aaaa=2025")
    fecha_hora.cambiar("HH=05")
    fecha_hora.cambiar("MM=20")
    fecha_hora.cambiar("SS=50")
    print(fecha_hora)

    fecha_hora.cambiar("dd=40")  # Día inválido
