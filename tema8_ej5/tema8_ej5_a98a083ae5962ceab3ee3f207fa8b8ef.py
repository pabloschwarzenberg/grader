class FechaHora:
    def __init__(self):
        self.aaaa=""
        self.mm=""
        self.dd=""
        self.HH=""
        self.MM=""
        self.SS=""

    def __str__(self):
        lista1=[self.aaaa,self.mm,self.dd]
        lista1="/".join(lista1)
        lista2=[self.HH,self.MM,self.SS]
        lista2=":".join(lista2)
        final=lista1+" "+lista2
        return final

    def fijarFecha(self, fecha):
        if ("/" in fecha) == True:
            fecha = fecha.split("/")
        elif (("-" in fecha) == True):
            fecha = fecha.split("-")
        self.dd=fecha[0]
        self.mm=fecha[1]
        self.aaaa=fecha[2]

    def fijarHora(self, hora):
        hora=hora.split(":")
        self.HH = hora[0]
        self.MM = hora[1]
        self.SS = hora[2]

    def fijarFechaHora(self, fechahora):
        fechahora=fechahora.split(" ")
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])

    def cambiar(self, parte):
        parte=parte.split("=")
        parte[0]=parte[0].strip()
        parte[1]=parte[1].strip()
        if parte[0]=="dd":
            self.dd=parte[1]
        elif parte[0]=="mm":
            self.mm=parte[1]
        elif parte[0]=="aaaa":
            self.aaaa=parte[1]
        elif parte[0]=="MM":
            self.MM=parte[1]
        elif parte[0]=="HH":
            self.HH=parte[1]
        elif parte[0]=="SS":
            self.SS=parte[1]



if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
