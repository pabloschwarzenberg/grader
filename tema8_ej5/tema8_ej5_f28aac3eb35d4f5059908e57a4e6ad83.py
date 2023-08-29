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
        parametro = parametro.replace(" ", "")
        tipo, valor = parametro.split("=")

        if tipo == "dd":
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.fecha = self.fecha[:2] + str(dia) + self.fecha[2:]
            else:
                print("Error: Día inválido")
        elif tipo == "mm":
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.fecha = self.fecha[:5] + str(mes) + self.fecha[6:]
            else:
                print("Error: Mes inválido")
        elif tipo == "aaaa":
            anio = int(valor)
            self.fecha = str(anio) + self.fecha[4:]
        elif tipo == "HH":
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = self.hora[:2] + str(hora) + self.hora[2:]
            else:
                print("Error: Hora inválida")
        elif tipo == "MM":
            minuto = int(valor)
            if minuto >= 0 and minuto <= 59:
                self.hora = self.hora[:5] + str(minuto) + self.hora[5:]
            else:
                print("Error: Minuto inválido")
        elif tipo == "SS":
            segundo = int(valor)
            if segundo >= 0 and segundo <= 59:
                self.hora = self.hora[:8] + str(segundo) + self.hora[8:]
            else:
                print("Error: Segundo inválido")
        else:
            print("Error: Parámetro inválido")

    def __repr__(self):
        return f"{self.fecha} {self.hora}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("31/12/2022")
    fecha_hora.fijarHora("23:59:59")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("01/01/2023 00:00:00")
    print(fecha_hora)

    fecha_hora.cambiar("dd=2")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("aaaa=2024")
    fecha_hora.cambiar("HH=25")
    fecha_hora.cambiar("MM=60")
    fecha_hora.cambiar("SS=70")
    print(fecha_hora)