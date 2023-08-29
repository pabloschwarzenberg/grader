class FechaHora:
    def __init__(self):
    
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        fecha=fecha.split("/")
        fecha=fecha.split("-")
        dia=fecha[0]
        mes=fecha[1]
        año=fecha[2]
        pass

    def fijarHora(self,hora):
        hora=hora.split(":")
        Hora=hora[0]
        minuto=hora[1]
        segundo=hora[2]
        pass

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        hora=fechahora.pop()
        fecha="".join(fechahora)
        hora=hora.split(":")
        if fecha.find("/")!=-1:
            fecha=fecha.split("/")
        else:
            fecha=fecha.split("-")
        Hora=hora[0]
        minuto=hora[1]
        segundo=hora[2]
        dia=fecha[0]
        print(fecha[0])
        mes=fecha[1]
        año=fecha[2]
        pass

    def cambiar(self,parte):
        if parte.find("dd")!=-1:
            parte=parte.split("=")
            dia=parte[1]
            return dia
        if parte.find("mm")!=-1:
            parte=parte.split("=")
            mes=parte[1]
            return mes
        if parte.find("aaaa")!=-1:
            parte=parte.split("=")
            año=parte[1]
            return año
        if parte.find("HH")!=-1:
            parte=parte.split("=")
            Hora=parte[1]
            return Hora
        if parte.find("MM")!=-1:
            parte=parte.split("=")
            minuto=parte[1]
            return minuto
        if parte.find("SS")!=-1:
            parte=parte.split("=")
            segundo=parte[1]
            return segundo
        
        pass
    def fecha():
        print( año+"/"+mes+"/"+dia+" "+Hora+":"+minuto+":"+segundo)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

    
           
