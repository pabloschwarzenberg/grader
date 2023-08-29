class FechaHora:
    def __init__(self):
        self.año=""
        self.mes=""
        self.dia=""
        self.hora=""
        self.minu=""
        self.segu=""
    def __str__(self):
        return self.año+"/"+self.mes+"/"+self.dia+"/"+self.hora+"/"+self.minu+"/"+self.segu+"/"
    def fijarFecha(self,fecha):
        if ("/" in fecha):
            fecha=fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        if ("-" in fecha):
            fecha=fecha.split("-")
            self.hora=fecha[0]
            self.minu=fecha[1]
            self.segu=fecha[2]
        pass
    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hora=hora[0]
        self.minu=hora[1]
        self.segu=hora[2]
        pass
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fecha=fechahora[0]
        if ("/" in fecha):
            fecha=fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        if ("-" in fecha):
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        pass
        hora=hora.split(":")
        self.hora=hora[0]
        self.minu=hora[1]
        self.segu=hora[2]
        pass
    def cambiar(self,parte):
        cambios=[]
        if parte[0]=="d":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.dia=cambios[h]
        if parte[0]=="m":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.mes==cambios[h]
        if parte[0]=="a":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.año=cambios[h]
        if parte[0]=="H":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.hora=cambios[h]
        if parte[0]=="M":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.minu=cambios[h]
        if parte[0]=="S":
            parte=parte.split("=")
            for m in parte:
                m=m.strip()
                cambios.append(m)
                h=len(camios)-1
                self.segu=cambios[h]
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           