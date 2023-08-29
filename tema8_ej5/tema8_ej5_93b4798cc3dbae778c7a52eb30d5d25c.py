class FechaHora:
    def __init__(self):
        self.fecha="0"
        self.hora="0"

    def fijarFecha(self,fecha):
        lista=self.fecha.split("-")
        self.fecha=lista[2]+"/"+lista[1]+"/"+lista[0]

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        a=fechahora.split(" ")
        self.fecha=a[0]
        lista=a[0].split("-")
        self.fecha=lista[2]+"/"+lista[1]+"/"+lista[0]
        self.hora=a[1]
        

    def cambiar(self,parte):
        lparte=parte.split("=")
        lparte[0]=lparte[0].strip(" ")
        lparte[1]=lparte[1].strip(" ")
     
        if lparte[0]=="dd":
            lista=self.fecha.split("/")
            lista[2]=lparte[1] 
            self.fecha=lista[0]+"/"+lista[1]+"/"+lista[2]
        if lparte[0]=="mm":
            lista=self.fecha.split("/")
            lista[1]=lparte[1] 
            self.fecha=lista[0]+"/"+lista[1]+"/"+lista[2]
        if lparte[0]=="aaaa":
            lista=self.fecha.split("/")
            lista[0]=lparte[1]
            self.fecha=lista[0]+"/"+lista[1]+"/"+lista[2]
        if lparte[0]=="HH":
            pass

    def __str__(self):
        return self.fecha+" "+self.hora

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
    