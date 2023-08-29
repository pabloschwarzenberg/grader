class FechaHora:
    def __init__(self):
        self.hora=""
        self.fecha=""
        return
    def __str__(self):
        return self.fecha+" "+self.hora

    def fijarFecha(self,fecha):
        dd=fecha[0]+fecha[1]
        mm=fecha[3]+fecha[4]
        aaaa=fecha[6]+fecha[7]+fecha[8]+fecha[9]
        self.fecha="{0}/{1}/{2}".format(aaaa,mm,dd)
        return dd,mm,aaaa

    def fijarHora(self,hora):
        HH=hora[0]+hora[1]
        MM=hora[3]+hora[4]
        SS=hora[6]+hora[7]
        self.hora="{0}:{1}:{2}".format(HH,MM,SS)
        return HH,MM,SS

    def fijarFechaHora(self,fechahora):
        dd=fechahora[0]+fechahora[1]
        mm=fechahora[3]+fechahora[4]
        aaaa=fechahora[6]+fechahora[7]+fechahora[8]+fechahora[9]
        HH=fechahora[11]+fechahora[12]
        MM=fechahora[14]+fechahora[15]
        SS=fechahora[17]+fechahora[18]
        
        self.fecha="{0}/{1}/{2}".format(aaaa,mm,dd)
        self.hora="{0}:{1}:{2}".format(HH,MM,SS)
        
        return dd,mm,aaaa,HH,MM,SS

    def cambiar(self,parte):
        if parte[0]=="d":
            parte=parte.split(" ")
            parte="".join(parte)
            fecha=self.fecha.split("/")
            dd=parte[3::]
            fecha[2]=dd
            fecha="/".join(fecha)
            self.fecha=fecha
            return dd
        if parte[0]=="m":
            parte=parte.split(" ")
            parte="".join(parte)
            fecha=self.fecha.split("/")
            mm=parte[3::]
            fecha[1]=mm
            fecha="/".join(fecha)
            self.fecha=fecha
            return mm
        if parte[0]=="a":
            parte=parte.split(" ")
            parte="".join(parte)
            aaaa=parte[5::]
            fecha=self.fecha.split("/")
            fecha[0]=aaaa
            fecha="/".join(fecha)
            self.fecha=fecha
            return aaaa
        if parte[0]=="H":
            parte=parte.split(" ")
            parte="".join(parte)
            hora=self.hora.split(":")
            HH=parte[3::]
            hora[0]=HH
            hora=":".join(hora)
            self.hora=hora
            return HH
        if parte[0]=="M":
            parte=parte.split(" ")
            parte="".join(parte)
            hora=self.hora.split(":")
            MM=parte[3::]
            hora[1]=MM
            hora=":".join(hora)
            self.hora=hora
            return MM
        if parte[0]=="S":
            parte=parte.split(" ")
            parte="".join(parte)
            hora=self.hora.split(":")
            SS=parte[3::]
            hora[2]=SS
            hora=":".join(hora)
            self.hora=hora
            return SS


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           