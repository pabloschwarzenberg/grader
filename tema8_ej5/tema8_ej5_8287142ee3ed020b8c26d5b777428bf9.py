class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split("=")
        tipo = partes[0].strip().lower()
        valor = partes[1].strip()
        
        if tipo == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Error: Día inválido")
            else:
                self.dia = int(valor)
        elif tipo == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Error: Mes inválido")
            else:
                self.mes = int(valor)
        elif tipo == "aaaa":
            self.anio = int(valor)
        elif tipo == "hh":
            if int(valor) < 0 or int(valor) > 23:
                print("Error: Hora inválida")
            else:
                self.hora = int(valor)
        elif tipo == "mm":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Minuto inválido")
            else:
                self.minuto = int(valor)
        elif tipo == "ss":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Segundo inválido")
            else:
                self.segundo = int(valor)
        else:
            print("Error: Parámetro inválido")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("25/06/2023")
    fecha_hora.fijarHora("08:30:00")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("15/12/2022 12:45:30")
    print(fecha_hora)

    fecha_hora.cambiar("dd=10")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("aaaa=2024")
    fecha_hora.cambiar("hh=25")
    fecha_hora.cambiar("mm=61")
    fecha_hora.cambiar("ss=45")
    print(fecha_hora)
