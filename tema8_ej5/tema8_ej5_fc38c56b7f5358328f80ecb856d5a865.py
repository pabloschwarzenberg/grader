class FechaHora:
    def __init__(self):
        self.dd = ""
        self.mm = ""
        self.aaaa = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""

    def __str__(self):
        return str(self.aaaa) + "/" + str(self.mm) + "/" + str(self.dd) + " " + str(self.HH) + ":" + str(self.MM) + ":" + str(self.SS)

    def fijarFecha(self, fecha):
        for i in fecha:
            if i == "-":
                self.dd, self.mm, self.aaaa = fecha.split("-")
            elif i == "/":
                self.dd, self.mm, self.aaaa = fecha.split("/")

    def fijarHora(self, hora):
        self.HH, self.MM, self.SS = hora.split(":")

    def fijarFechaHora(self, fechahora):
        fecha,hora = fechahora.split(" ")
        for i in fechahora:
            if i == "-":
                self.dd, self.mm, self.aaaa = fecha.split("-")
            if i == "/":
                self.dd, self.mm, self.aaaa = fecha.split("/")
        self.HH, self.MM, self.SS = hora.split(":")

    def cambiar(self,parte):
        if "=" in parte:
            p,parte = parte.split("=")
        if " = " in parte:
            p,parte= parte.split(" = ")
        h = int(parte)
        if p == "dd" and 1 <= h <= 31:
            self.dd = h
        if p == "mm" and 1 <= h <= 12:
            self.mm = h
        if p == "aaaa":
            self.aaaa = h
        if p == "HH" and 0 <= h <= 24:
            self.HH = h
        if p == "MM" and 1 <= h <= 12:
            self.MM = h
        if p == "SS" and 1 <= h <= 12:
            self.SS = h

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

