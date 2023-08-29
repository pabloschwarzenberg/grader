class FechaHora:
    def __init__(self,dd=1,mm=1,aaaa=1,HH=1,MM=1,SS=1):
        self.dd=dd
        self.mm=mm
        self.aaaa=aaaa
        self.HH=HH
        self.MM=MM
        self.SS=SS
    def __str__(self):
        return str(self.aaaa)+"/"+str(self.mm)+"/"+str(self.dd)+" "+str(self.HH)+":"+str(self.MM)+":"+str(self.SS)

    def fijarFecha(self,fecha):
        if ("-" in fecha)==True:
            fecha=fecha.split("-")
            self.dd=fecha[0]
            self.mm=fecha[1]
            self.aaaa=fecha[2]
        elif ("/" in fecha)==True:
            fecha=fecha.split("/")
            self.dd=fecha[0]
            self.mm=fecha[1]
            self.aaaa=fecha[2]

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.HH=hora[0]
        self.MM=hora[1]
        self.SS=hora[2]
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        if "/" in fechahora[0]:
            a=fechahora[0].split("/")
        else:
            a=fechahora[0].split("-")
        b=fechahora[1].split(":")
        self.dd=a[0]
        self.mm=a[1]
        self.aaaa=a[2]
        self.HH=b[0]
        self.MM=b[1]
        self.SS=b[2]
    def cambiar(self,parte):
        parte=parte.split("=")
        b=""
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        for i in parte[1]:
            if i in numeros:
                b=b+i
        if ("dd" in parte[0])==True:
            if self.mm==1 or self.mm==3 or self.mm==5 or self.mm==7 or self.mm==8 or self.mm==10 or self.mm==12:
                if int(b)>31 or int(b)<1:
                    return False
                else:
                    self.dd=int(b)
            elif self.mm==4 or self.mm==6 or self.mm==9 or self.mm==11:
                if int(b)>30 or int(b)<1:
                    return False
                else:
                    self.dd=int(b)
            elif self.mm==2:
                if int(b)>28 or int(b)<1:
                    return False
                else:
                    self.dd=int(b)
        elif ("mm" in parte[0])==True:
            if int(b)>12 or int(b)<1:
                return False
            else:
                self.mm=int(b)
        elif ("aaaa" in parte[0]) ==True:
            self.aaaa=int(b)
        elif ("HH" in parte[0])==True:
            if int(b)>=24 or int(b)<1:
                return False
            else:
                self.HH=int(b)
        elif ("MM" in parte[0])==True:
            if int(b)>=60 or int(b)<1:
                return False
            else:
                self.MM=int(b)
        elif ("SS" in parte[0])==True:
            if int(b)>=60 or int(b)<1:
                return False
            else:
                self.SS=int(b)
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30/09/2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)