class FechaHora:
    def __init__(self,dd=0,mm=0,aaaaa=0,h=0,m=0,s=0):
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaaa
        self.HH = h
        self.MM = m
        self.SS = s

    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(str(self.aaaa),str(self.mm),str(self.dd),str(self.HH),str(self.MM),str(self.SS))

    def fijarFecha(self,fecha):
        a = fecha[2]
        f = fecha.split("{0}".format(a))
        self.dd,self.mm,self.aaaa = f[0],f[1],f[2]
        
    def fijarHora(self,hora):
        h = hora.split(":")
        self.HH,self.MM,self.SS = h[0],h[1],h[2]

    def fijarFechaHora(self,fechahora):
        fh = fechahora.split(" ")
        self.fijarFecha(fh[0])
        self.fijarHora(fh[1])

    def cambiar(self,parte):
        p = parte.split("=")
        p[0] = p[0].strip()
        p[1] = p[1].strip()
        if p[0] == "dd":
            self.dd = p[1]
        if p[0] == "mm":
            self.mm = p[1]
        if p[0] == "aaaa":
            self.aaaa = p[1]
        if p[0] == "HH":
            self.HH = p[1]
        if p[0] == "MM":
            self.MM = p[1]
        if p[0] == "SS":
            self.SS = p[1]
        
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           