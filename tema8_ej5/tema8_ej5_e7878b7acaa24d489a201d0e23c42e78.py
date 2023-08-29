class FechaHora:
    def __init__(self):
        self.HH=""
        self.MM=""
        self.SS=""
        self.dd=""
        self.mm=""
        self.aaaa=""
        
    def __str__(self):
        return self.fechahora

    def fijarFecha(self,fecha):
        lista7=fecha.split("/")
        lista7=fecha.split("-")
        self.dd=lista7[0]
        self.mm=lista7[1]
        self.aaaa=lista7[2]
        

    def fijarHora(self,hora):
        lista6=hora.split(":")
        self.HH=lista6[0]
        self.MM=lista6[1]
        self.SS=lista6[2]

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora
        lista1=fechahora.split(" ")
        self.hora=lista1[1]
        self.fecha=lista1[0]
        lista=self.fecha.split("/")
        lista=self.fecha.split("-")
        self.dd=lista[0]
        self.mm=lista[1]
        self.aaaa=lista[2]
        lista2=self.hora.split(":")
        self.HH=lista2[0]
        self.MM=lista2[1]
        self.SS=lista2[2]
        self.fechahora=str(self.aaaa+"/"+self.mm+"/"+self.dd+" "+self.HH+":"+self.MM+":"+self.SS)
        
    def cambiar(self,parte):
        if "=" in parte:
            p=parte.split("=")
            if " = " in parte: 
                p=parte.split(" = ")
        if p[0]=="mm":
            self.mm=p[1]
            
        if p[0]=="aaaa":
            self.aaaa=p[1]
            
        elif p[0]=="dd":
            self.dd=p[1]
            
        elif p[0]=="HH":
            self.HH=p[1]
            
        elif p[0]=="MM":
            self.MM=p[1]
            
        elif p[0]=="SS":
            self.SS=p[1]

        self.fechahora=str(self.aaaa+"/"+self.mm+"/"+self.dd+" "+self.HH+":"+self.MM+":"+self.SS)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           