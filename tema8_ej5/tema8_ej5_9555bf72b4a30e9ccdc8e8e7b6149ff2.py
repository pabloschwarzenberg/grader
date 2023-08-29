class FechaHora:
    def __init__(self):
        self.aa=0
        self.mm=0
        self.dd=0
        self.HH=0
        self.MM=0
        self.SS=0

    def __str__(self):
        s="{:0>4}/{:0>2}/{:0>2} {:0>2}:{:0>2}:{:0>2}".format(self.aa,self.mm,self.dd,self.HH,self.MM,self.SS)
        return s

    def fijarFecha(self,fecha):
        if "/" in fecha:
            fecha=fecha.split("/")
        elif "-" in fecha:
            fecha=fecha.split("-")
        self.dd=fecha[0]
        self.mm=fecha[1]
        self.aa=fecha[2]

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.HH=hora[0]
        self.MM=hora[1]
        self.SS=hora[2]

    def fijarFechaHora(self,fechahora):
        fechaHora=fechahora.split(" ")
        fecha=fechaHora[0]
        hora=fechaHora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,parte):
        tipo=parte.split("=")[0]
        dato=parte.split("=")[1]
        dato=int(dato)
        if tipo=="aaaa":
            self.aa=dato
        elif tipo=="mm":
            if dato>12:
                print("NO")
                return False
            self.mm=dato
        elif tipo=="dd":
            if dato>31:
                print("NO")
                return False
            self.dd=dato
        elif tipo=="HH":
            if dato>24:
                print("NO")
                return False
            self.HH=dato
        elif tipo=="MM":
            if dato>60:
                print("NO")
                return False
            self.MM=dato
        elif tipo=="SS":
            if dato>60:
                print("NO")
                return False
            self.SS=dato
            
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           