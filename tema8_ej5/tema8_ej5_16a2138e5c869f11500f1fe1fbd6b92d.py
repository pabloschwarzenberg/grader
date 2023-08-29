class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("/"))
        elif "-" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("-"))
        else:
            print("Formato de fecha inválido")

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        parametro, valor = parametro.split("=")

        if parametro == "dd":
            valor = int(valor)
            if 1 <= valor <= 31:
                self.dia = valor
            else:
                print("Día inválido")
        elif parametro == "mm":
            valor = int(valor)
            if 1 <= valor <= 12:
                self.mes = valor
            else:
                print("Mes inválido")
        elif parametro == "aaaa":
            valor = int(valor)
            if valor >= 1900:
                self.anio = valor
            else:
                print("Año inválido")
        elif parametro == "HH":
            valor = int(valor)
            if 0 <= valor <= 23:
                self.hora = valor
            else:
                print("Hora inválida")
        elif parametro == "MM":
            valor = int(valor)
            if 0 <= valor <= 59:
                self.minuto = valor
            else:
                print("Minuto inválido")
        elif parametro == "SS":
            valor = int(valor)
            if 0 <= valor <= 59:
                self.segundo = valor
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")

    def __str__(self):
        return f"{self.anio}/{self.mes}/{self.dia} {self.hora}:{self.minuto}:{self.segundo}"
