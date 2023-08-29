class FechaHora:
    def __init__(self):
        self.dd = ""
        self.mm = ""
        self.aaaa = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""

    def __str__(self):
        return ("{0}/{1}/{2} {3}:{4}:{5}".format(self.aaaa, self.mm, self.dd, self.HH, self.MM, self.SS))

    def fijarFecha(self, fecha):
        pass
    def fijarHora(self, hora):
        self.HH = hora[0:2]
        self.MM = hora[3:5]
        self.SS = hora[6:8]

    def fijarFechaHora(self, fechahora):
        f = fechahora.split(" ")
        a = "".join(f)
        self.aaaa = a[6:10]
        self.mm = a[3:5]
        self.dd = a[0:2]
        self.HH = a[10:12]
        self.MM = a[13:15]
        self.SS = a[16:18]
        return ("{0}/{1}/{2} {3}:{4}:{5}".format(self.aaaa, self.mm, self.dd, self.HH, self.MM, self.SS))
    def cambiar(self, parte):
        if parte[0:2]=="mm":
            self.mm = parte[3:5]
        elif parte[0:4]=="aaaa":
            self.aaaa = parte[7:11]
if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

