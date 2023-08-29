class FechaHora:
    def __init__(self):
        self.dia=""
        self.mes=""
        self.año=""
        self.seg=""
        self.min=""
        self.hr=""
    def fijarFecha(self,fecha):
        a=fecha.count("-")
        b=fecha.count("/")
        if a!=0:
            fecha.split("-")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        elif b!=0:
            fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hr=hora[0]
        self.min=hora[1]
        self.seg=hora[2]
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.replace("/"," ")
        fechahora=fechahora.replace("-"," ")
        fechahora=fechahora.replace(":"," ")
        fechahora=fechahora.split(" ")
        if " " in fechahora is True:
            fechahora=fechahora.remove(" ")
        self.dia=fechahora[0]
        self.mes=fechahora[1]
        self.año=fechahora[2]
        self.hr=fechahora[3]
        self.min=fechahora[4]
        self.seg=fechahora[5]
    def cambiar(self,parte):
        #el split lo puedes hacer directamente por el igual =
        #luego usas strip para sacar caracteres en blanco
        #por ejemplo cuando se ingresa
        #aaaa = 2016
        parte=parte.split("=")
        parte[0]=parte[0].strip()
        parte[1]=parte[1].strip()
        if parte[0]=="dd":
            if int(parte[1])<32:
                self.dia=parte[1]
            else:
                print("Día no válido")
        elif parte[0]=="mm":
            if int(parte[1])<13:
                self.mes=parte[1]
            else:
                print("Mes no válido")
        elif parte[0]=="aaaa":
            self.año=int(parte[1])
        elif parte[0]=="HH":
            if int(parte[1])<25:
                self.hr=parte[1]
            else:
                print("Hora no válido")
        elif parte[0]=="MM":
            if int(parte[1])<61:
                self.min=parte[1]
            else:
                print("Minuto no válido")
        elif parte[0]=="SS":
            if int(parte[1])<61:
                self.seg=parte[1]
            else:
                print("Segundo no válido")
    def __str__(self):
        a=str(self.año)+"/"+self.mes+"/"+self.dia+" "+self.hr+":"+self.min+":"+self.seg
        return a

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)