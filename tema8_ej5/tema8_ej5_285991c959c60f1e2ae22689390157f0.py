class FechaHora:
    def __init__(self):
        self.SS=""
        self.MM=""
        self.HH=""
        self.dd=""
        self.mm=""
        self.aaaa=""

    def __str__(self):
        
        return str(self.aaaa)+"/"+str(self.mm)+"/"+str(self.dd)+" "+str(self.HH)+":"+str(self.MM)+":"+str(self.SS) 

    def fijarFecha(self,fecha):
        for separador in fecha:
            if separador=="/":
                self.dd,self.mm,self.aaaa=fecha.split("/")

            elif separador=="-":
                self.dd,self.mm,self.aaaa=fecha.split("-")
                
       
                

    def fijarHora(self,hora):
        self.HH,self.MM,self.SS=hora.split(":")

    def fijarFechaHora(self,fechahora):
        fecha,hora=fechahora.split(" ")
        for separador in fecha:
            if separador=="/":
                self.dd,self.mm,self.aaaa=fecha.split("/")

            elif separador=="-":
                self.dd,self.mm,self.aaaa=fecha.split("-")

        self.HH,self.MM,self.SS=hora.split(":")

    def cambiar(self,parte):
        #for i in parte:
        if " = " in parte:
           parametro,parte=parte.split(" = ")

        if "=" in parte:
            parametro,parte=parte.split("=")
        
        parte=int(parte)
        if parametro=="SS":
            if 0<=parte<=60:
                self.SS=parte
        elif parametro=="MM":
            if 0<=parte<=60:
                self.MM=parte
        elif parametro=="HH":
            if 0<=parte<=60:
                self.HH=parte
        elif parametro=="dd":
            if 0<=parte<=31:
                self.dd=parte
        elif parametro=="mm":
            if 1<=parte<=12:
                self.mm=parte
        elif parametro=="aaaa":
            self.aaaa=parte

        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           