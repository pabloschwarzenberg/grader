class FechaHora:
    def __init__(self):
        self.ano = 0
        self.mes = 0
        self.dia = 0
        self.hor = 0
        self.min = 0
        self.seg = 0

    def fijarFecha(self,fecha):
        if fecha[2] == "/":
            l = fecha.split("/")
        else:
            l = fecha.split("-")
        self.ano = l[0]
        self.mes = l[1]
        self.dia = l[2]

    def fijarHora(self,hora):
        H = hora.split(":")
        self.hor = H[0]
        self.min = H[1]
        self.seg = H[2]

    def fijarFechaHora(self,fechahora):
        a = fechahora
        b = a.split(" ")
        c1 = b[0].split("-")
        c2 = b[1].split(":")
        self.ano = c1[2]
        self.mes = c1[1]
        self.dia = c1[0]
        self.hor = c2[0]
        self.min = c2[1]
        self.seg = c2[2]

    def cambiar(self,parte):
        if parte[0] == "a":
            self.ano = parte[7:11]
        elif parte[0] == "m":
            self.mes = parte[3:5]
        else:
            pass

    def __str__(self):
        return str(self.ano)+"/"+str(self.mes)+"/"+str(self.dia)+" "+str(self.hor)+":"+str(self.min)+":"+str(self.seg)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)