class FechaHora:
    def __init__(self):
        self.dd=""
        self.mm=""
        self.aaaa=""
        self.HH=""
        self.MM=""
        self.SS=""
        pass

    def __str__(self):
        return (self.aaaa+"/"+self.mm+"/"+self.dd+" "+self.HH+":"+self.MM+":"+self.SS)

    def fijarFecha(self, fecha):
        if fecha.find("/")!=-1:
            fecha=fecha.split("/")
        elif fecha.find("-") != -1:
            fecha = fecha.split("-")
        self.aaaa=fecha[2]
        self.dd=fecha[0]
        self.mm=fecha[1]
        pass

    def fijarHora(self, hora):
        hora=hora.split(":")
        self.HH=hora[0]
        self.MM=hora[1]
        self.SS=hora[2]
        pass

    def fijarFechaHora(self, fechahora):
        fh=FechaHora()
        fechahora=fechahora.split(" ")
        fh.fijarFecha(fechahora[0])
        fh.fijarHora(fechahora[1])
        pass

    def cambiar(self, parte):
        dato=0
        parte=parte.split("=")
        datos=["aaaa","dd","mm","HH","MM","SS"]
        for i in range (len(datos)):
            if parte[0]==datos[i]:
                dato=i

        if dato==0:
            self.aaaa=parte[1]
        elif dato==1:
            self.dd=parte[1]
        elif dato==2:
            self.mm=parte[1]
        elif dato==3:
            self.HH=parte[1]
        elif dato==4:
            self.MM=parte[1]
        elif dato==5:
            self.SS=parte[1]
        pass


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
