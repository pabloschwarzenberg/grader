class FechaHora:
    def __init__(self):
        self.h=""
        self.mi=""
        self.s=""
        self.d=""
        self.me=""
        self.a=""

    def __str__(self):
        u=str(self.a)+"/"+str(self.me)+"/"+str(self.d)+" "+str(self.h)+":"+str(self.mi)+":"+str(self.s)
        return u

    def fijarFecha(self,fecha):
        self.d=fecha[:2]
        self.me=fecha[3:5]
        self.a=fecha[6:]

    def fijarHora(self,hora):
        self.h=hora[:2]
        self.mi=hora[3:5]
        self.s=hora[6:]
        
    def fijarFechaHora(self,fechahora):
        self.d=fechahora[:2]
        self.me=fechahora[3:5]
        self.a=fechahora[6:10]
        self.h=fechahora[11:13]
        self.mi=fechahora[14:16]
        self.s=fechahora[17:]

    def cambiar(self,parte):
        if parte[:2]=="dd":
            self.d=parte[3:5]
            return self.d
        elif parte[:2]=="mm":
            self.me=parte[3:5]
            return self.me
        elif parte[:2]=="aa":
            self.a=parte[7:11]
            return self.a
        elif parte[:2]=="HH":
            self.h=parte[3:5]
            return self.h
        elif parte[:2]=="MM":
            self.mi=parte[3:5]
            return self.mi
        elif parte[:2]=="SS":
            self.s=parte[3:5]
            return self.s

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)