class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
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
        parametro, valor = parte.split("=")
        parametro = parametro.strip().lower()
        valor = int(valor.strip())

        if parametro == "dd":
            if valor >= 1 and valor <= 31:
                self.dia = valor
            else:
                print("Día inválido")
        elif parametro == "mm":
            if valor >= 1 and valor <= 12:
                self.mes = valor
            else:
                print("Mes inválido")
        elif parametro == "aaaa":
            if valor >= 1 and valor <= 9999:
                self.anio = valor
            else:
                print("Año inválido")
        elif parametro == "hh":
            if valor >= 0 and valor <= 23:
                self.hora = valor
            else:
                print("Hora inválida")
        elif parametro == "min":
            if valor >= 0 and valor <= 59:
                self.minuto = valor
            else:
                print("Minuto inválido")
        elif parametro == "ss":
            if valor >= 0 and valor <= 59:
                self.segundo = valor
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")



if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
