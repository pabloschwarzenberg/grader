class FechaHora:
    def __init__(self):
        self.dia=""
        self.mes=""
        self.año=""
        self.hora=""
        self.minu=""
        self.segun=""
        pass

    def __str__(self):
        return self.año+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minu+":"+self.segun

    def fijarFecha(self,fecha):
        if ("/" in fecha):
            fecha=fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        elif("-" in fecha):
            fecha=fecha.split("-")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        pass

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hora=hora[0]
        self.minu=hora[1]
        self.segun=hora[2]
        pass

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fecha=fechahora[0]
        if ("/" in fecha):
            fecha=fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        elif("-" in fecha):
            fecha=fecha.split("-")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.año=fecha[2]
        hora=fechahora[1]
        hora=hora.split(":")
        self.hora=hora[0]
        self.minu=hora[1]
        self.segun=hora[2]
        pass

    def cambiar(self,parte):
        lista=[]
        if parte[0]=="d":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.dia=lista[ja]
        elif parte[0]=="m":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.mes=lista[ja]
        elif parte[0]=="a":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.año=lista[ja]
        elif parte[0]=="H":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.hora=lista[ja]
        elif parte[0]=="M":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.minu=lista[ja]
        elif parte[0]=="S":
            parte=parte.split("=")
            for i in parte:
                i=i.strip()
                lista.append(i)
                ja=len(lista)-1
                self.segun=lista[ja]
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFecha("30-09-2015")
    print(fh)
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
