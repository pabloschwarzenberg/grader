class FechaHora:
    def __init__(self):
        self.aaaa=""
        self.mm=""
        self.dd=""
        self.HH=""
        self.MM=""
        self.SS=""

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.aaaa,self.mm,self.dd,self.HH,self.MM,self.SS)
        
    def fijarFecha(self,fecha):
        if "-" in fecha:
          fecha=fecha.split("-")
          self.dd+=fecha[0]
          self.mm+=fecha[1]
          self.aaaa+=fecha[2]
        else:
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
        fecha=fechahora[0]
        hora=fechahora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,parte):
        parte=parte.split("=")
        if parte[0]=="aaaa" or parte[0]=="aaaa ":
            a=parte[1].split(" ")
            self.aaaa=a[1]
        if parte[0]=="mm":
            self.mm=parte[1]
        if parte[0]=="dd":
            self.dd=parte[1]
        if parte[0]=="HH":
            self.HH=parte[1]
        if parte[0]=="MM":
            self.MM=parte[1]
        if parte[0]=="SS":
            self.SS=parte[1]
            

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           