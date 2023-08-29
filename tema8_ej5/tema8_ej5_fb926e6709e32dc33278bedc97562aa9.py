class FechaHora:
    def __init__(self):
        self.dia=0
        self.mes=0
        self.year=0
        self.segundo=0
        self.minuto=0
        self.hora=0

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(str(self.year),str(self.mes),str(self.dia),str(self.hora),str(self.minuto),str(self.segundo))

    def fijarFecha(self,fecha):
        fecha=fecha.strip()
        fecha=fecha.replace("/","-")
        fecha=fecha.split("-")
        self.dia=fecha[0]
        self.mes=fecha[1]
        self.year=fecha[2]

    def fijarHora(self,hora):
        hora=hora.strip().split(":")
        self.hora=hora[0]
        self.minuto=hora[1]
        self.segundo=hora[2]
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split()
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])

    def cambiar(self,parte):
        parte=parte.replace(" ","").split("=")
        if parte[0]=="dd":
            if 0<=int(parte[1])<=31:
                self.dia=int(parte[1])
        elif parte[0]=="mm":
            if 0<=int(parte[1])<=12:
                self.mes=int(parte[1])
        elif parte[0]=="aaaa":
            self.year=int(parte[1])
        elif parte[0]=="HH":
            if int(parte[0])<=24:
                self.hora=parte[0]
        elif parte[0]=="MM":
            if int(parte[1])<60:
                self.minuto=parte[1]
        elif parte[0]=="SS":
            if int(parte[1])<60:
                self.segundo=parte[1]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           