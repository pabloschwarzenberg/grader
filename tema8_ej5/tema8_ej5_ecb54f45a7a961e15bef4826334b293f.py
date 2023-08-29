class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
        self.fechahora = None

    def fijarFecha(self, string):
        self.fecha = string
        self.fecha.split("/")

    def fijarHora(self, string):
        self.hora = string
        self.hora.split(":")

    def fijarFechaHora(self, string):
        a = string
        l = a.split(" ")
        self.fechahora = []
        contador1 = 0
        contador2 = 0
        for i in list(l[0]):
            if i == "/":
                contador1 += 1
            elif i == "-":
                contador2 += 1
        if contador1 == 2:
            self.fechahora.append(l[0].split("/"))
        if contador2 == 2:
            self.fechahora.append(l[0].split("-"))

        self.fechahora.append(l[1].split(":"))
        print( self.fechahora)

    def cambiar(self, magia):
        lol = magia.split("=")
        if lol[0] == "dd":
            self.fechahora[0][0] = lol[1]
        if lol[0] == "mm":
            self.fechahora[0][1] = lol[1]
        if lol[0] == "aaaa":
            self.fechahora[0][2] = lol[1]
        if lol[0] == "HH":
            self.fechahora[1][0] = lol[1]
        if lol[0] == "MM":
            self.fechahora[1][1] = lol[1]
        if lol[0] == "SS":
            self.fechahora[1][2] = lol[1]
        return self.fechahora

    def __str__(self):
        a = self.fechahora[0]
        a.reverse()
        b = "/".join(a)
        c = self.fechahora[1]
        d = ":".join(c)
        return b+" "+d

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           