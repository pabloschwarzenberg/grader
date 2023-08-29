class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def __str__(self):
        return self.anio+"/"+self.mes+"/"+self.dia + " " + self.hora + ":" + self.minuto + ":" + self.segundo

    def fijarFecha(self,fecha):
        if "/" in fecha:
            fecha = fecha.split("/")
        elif "-" in fecha:
            fecha = fecha.split("-")

        self.dia = fecha[0]
        self.mes = fecha[1]
        self.anio = fecha[2]

    def fijarHora(self,hora):
        hora = hora.split(":")
        self.hora = hora[0]
        self.minuto = hora[1]
        self.segundo = hora[2]

    def fijarFechaHora(self,fechahora):
        fechahora = fechahora.split(" ")
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])

    def cambiar(self,parte):
        parametro, valor = parte.replace(" ", "").split("=")
        if parametro == "dd":
            self.dia = valor
        elif parametro == "mm":
            self.mes = valor
        elif parametro == "aaaa":
            self.anio = valor
        elif parametro == "HH":
            self.hora = valor
        elif parametro == "MM":
            self.minuto = valor
        elif parametro == "SS":
            self.segundo = valor
        else:
            print("Error: parametro no valido")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           