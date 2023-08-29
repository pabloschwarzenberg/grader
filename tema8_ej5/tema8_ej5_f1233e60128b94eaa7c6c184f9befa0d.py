class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")

        if len(partes) != 3:
            print("Error: Formato de fecha incorrecto.")
            return

        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        if len(partes) != 3:
            print("Error: Formato de hora incorrecto.")
            return

        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        if len(partes) != 2:
            print("Error: Formato de fecha y hora incorrecto.")
            return

        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        partes = parte.split("=")
        if len(partes) != 2:
            print("Error: Formato de cambio incorrecto.")
            return

        atributo = partes[0].strip()
        valor = partes[1].strip()

        if atributo == "dd":
            dia = int(valor)
            if

           