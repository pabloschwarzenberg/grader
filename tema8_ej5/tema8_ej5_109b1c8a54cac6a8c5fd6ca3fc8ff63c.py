class FechaHora:
    def __init__(self):
        self.hora=[]
        self.fecha=[]

    def __str__(self):
        return self.fecha[2]+"/"+self.fecha[1]+"/"+self.fecha[0]+" "+self.hora[0]+":"+ self.hora[1]+":"+self.hora[2]

    def fijarFecha(self,fecha):
        fecha=fecha.split("-")
        self.fecha=fecha

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hora=hora
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fecha=fechahora[0]
        fecha=fecha.split("-")
        self.fecha=fecha
        hora=fechahora[1]
        hora=hora.split(":")
        self.hora=hora

    def cambiar(self,parte):
        parte=parte.split("=")
        indicador=parte[0].strip()
        valor=parte[1].strip()
        if indicador=="dd":
            self.fecha[0]=valor
        if indicador=="mm":
            self.fecha[1]=valor
        if indicador=="aaaa":
            self.fecha[2]=valor
        if indicador=="HH":
            self.hora[0]=valor
        if indicador=="MM":
            self.hora[1]=valor
        if indicador=="SS":
            self.hora[2]=valor

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)