class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
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
        fecha = partes[0].split("-")
        self.fijarFecha("{}/{}/{}".format(fecha[2], fecha[1], fecha[0]))
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        parametros = parte.split("=")
        parametro = parametros[0].strip()
        valor = int(parametros[1].strip())

        if parametro == "dd":
            if valor >= 1 and valor <= 31:
                self.dia = valor
            else:
                print("Error: El valor del día debe estar entre 1 y 31.")
        elif parametro == "mm":
            if valor >= 1 and valor <= 12:
                self.mes = valor
            else:
                print("Error: El valor del mes debe estar entre 1 y 12.")
        elif parametro == "aaaa":
            if valor >= 1 and valor <= 9999:
                self.anio = valor
            else:
                print("Error: El valor del año debe estar entre 1 y 9999.")
        elif parametro == "HH":
            if valor >= 0 and valor <= 23:
                self.hora = valor
            else:
                print("Error: El valor de la hora debe estar entre 0 y 23.")
        elif parametro == "MM":
            if valor >= 0 and valor <= 59:
                self.minuto = valor
            else:
                print("Error: El valor del minuto debe estar entre 0 y 59.")
        elif parametro == "SS":
            if valor >= 0 and valor <= 59:
                self.segundo = valor
            else:
                print("Error: El valor del segundo debe estar entre 0 y 59.")
        else:
            print("Error: Parámetro inválido.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
