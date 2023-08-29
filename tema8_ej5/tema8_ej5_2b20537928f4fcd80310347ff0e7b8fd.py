class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = fecha.split("/")
        elif "-" in fecha:
            self.dia, self.mes, self.anio = fecha.split("-")

        self.dia = int(self.dia)
        self.mes = int(self.mes)
        self.anio = int(self.anio)

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = hora.split(":")
        self.hora = int(self.hora)
        self.minuto = int(self.minuto)
        self.segundo = int(self.segundo)

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        variable, valor = parametro.split("=")
        valor = int(valor)

        if variable == "dd":
            if valor < 1 or valor > 31:
                print("Día inválido")
            else:
                self.dia = valor
        elif variable == "mm":
            if valor < 1 or valor > 12:
                print("Mes inválido")
            else:
                self.mes = valor
        elif variable == "aaaa":
            self.anio = valor
        elif variable == "HH":
            if valor < 0 or valor > 23:
                print("Hora inválida")
            else:
                self.hora = valor
        elif variable == "MM":
            if valor < 0 or valor > 59:
                print("Minuto inválido")
            else:
                self.minuto = valor
        elif variable == "SS":
            if valor < 0 or valor > 59:
                print("Segundo inválido")
            else:
                self.segundo = valor
        else:
            print("Parámetro inválido")

    def __repr__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("13/06/2023")
    fecha_hora.fijarHora("15:30:00")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("25/12/2023 18:45:30")
    print(fecha_hora)

    fecha_hora.cambiar("dd=20")
    fecha_hora.cambiar("mm=15")
    fecha_hora.cambiar("HH=10")
    fecha_hora.cambiar("MM=30")
    fecha_hora.cambiar("SS=55")
    fecha_hora.cambiar("aaaa=2022")
    fecha_hora.cambiar("xx=123")

    print(fecha_hora)
