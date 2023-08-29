class FechaHora:
    def __init__(self):
        self.dd = ""
        self.mm = ""
        self.aaaa = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""

    def __str__(self):
        str_objer = str(self.aaaa) + "/" + str(self.mm) + "/" + str(self.dd) + " " + str(self.HH) + ":" + str(self.MM) + ":" + str(self.SS)
        return str_objer

    def fijarFechaHora(self, diaHora): #"30-09-2015 17:45:00"
        diaHora = diaHora.split(" ")
        fecha = diaHora[0]
        fecha = fecha.split("-")
        self.dd = fecha[0]
        self.mm = fecha[1]
        self.aaaa = fecha[2]

        hora = diaHora[1]
        hora = hora.split(":")
        self.HH = hora[0]
        self.MM = hora[1]
        self.SS = hora[2]

        self.fechafijada = diaHora[0]
        self.horafijada = diaHora[1]


    def cambiar(self, fijarFecha): #"mm=10"
        fijarFecha = fijarFecha.split("=")
        if fijarFecha[0] == "mm":
            self.mm = fijarFecha[1]
        else:
            x = fijarFecha[1].split(" ")
            self.aaaa = x[1]

    def fijarFecha(self):
        self.fijarfecha = str(self.dd) + "/" + str(self.mm) + "/" + str(self.aaaa)


    def fijarHora(self, horas): #"18:00:00"
        horas = horas.split(":")
        self.HH = horas[0]
        self.MM = horas[1]
        self.SS = horas[2]
        self.fijarhora = str(self.HH) + ":" + str(self.MM) + ":" + str(self.SS)


if (__name__) == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)