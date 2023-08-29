class FechaHora:
    def __init__(self,fecha,hora,fechahora):
        self.fecha=""
        self.hora=""
        self.fechahora=""    
    def __str__(self):
        return "{0}".format(self.fechahora)

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        fechahora=self.fechahora.split(" ")
        fechahora[1]=hora
        self.fechahora=fechahora
        
    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora

    def cambiar(self,parte):
        x=self.fechahora
        x=x.split(" ")
        fecha=x[0]
        fecha=fecha.split("-")
        hora=x[1]
        hora=hora.split(":")
        if "dd" in parte:
            parte=list(parte)
            parte.remove("d")
            parte.remove("d")
            parte.remove("=")
            parte="".join(parte)
            fecha[0]=parte
        elif "mm" in parte:
            parte=list(parte)
            parte.remove("m")
            parte.remove("m")
            parte.remove("=")
            parte="".join(parte)
            fecha[1]=parte
        elif "aaaa" in parte:
            parte=list(parte)
            parte.remove("a")
            parte.remove("a")
            parte.remove("a")
            parte.remove("a")
            parte.remove("=")
            parte="".join(parte)
            fecha[2]=parte
            
        elif "HH" in parte:
            parte=list(parte)
            parte.remove("H")
            parte.remove("H")
            parte.remove("=")
            parte="".join(parte)
            hora[0]=parte

        elif "MM" in parte:
            parte=list(parte)
            parte.remove("M")
            parte.remove("M")
            parte.remove("=")
            parte="".join(parte)
            hora[1]=parte

        elif "SS" in parte:
            parte=list(parte)
            parte.remove("S")
            parte.remove("S")
            parte.remove("=")
            parte="".join(parte)
            hora[2]=parte 



        fecha="-".join(fecha)
        hora=":".join(hora)
        x=fecha+" "+hora
        self.fechahora=x
 

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           