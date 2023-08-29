class FechaHora:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.anio = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )

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

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        parte = parte.replace(" ", "")  # Eliminar espacios en blanco
        parametro, valor = parte.split("=")
        parametro = parametro.lower()
        valor = int(valor)

        if parametro == "dd":
            if valor < 1 or valor > 31:
                print("Error: El día debe estar entre 1 y 31.")
            else:
                self.dia = valor
        elif parametro == "mm":
            if valor < 1 or valor > 12:
                print("Error: El mes debe estar entre 1 y 12.")
            else:
                self.mes = valor
        elif parametro == "aaaa":
            self.anio = valor
        elif parametro == "hh":
            if valor < 0 or valor > 23:
                print("Error: La hora debe estar entre 0 y 23.")
            else:
                self.hora = valor
        elif parametro == "mn":
            if valor < 0 or valor > 59:
                print("Error: Los minutos deben estar entre 0 y 59.")
            else:
                self.minuto = valor
        elif parametro == "ss":
            if valor < 0 or valor > 59:
                print("Error: Los segundos deben estar entre 0 y 59.")
            else:
                self.segundo = valor
        else:
            print("Error: Parámetro no válido.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)