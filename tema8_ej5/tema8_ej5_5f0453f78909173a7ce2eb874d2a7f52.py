class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        self.fecha=fecha
        pass

    def fijarHora(self,hora):
        self.hora=hora
        pass

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora
        pass

    def cambiar(self,parte):
        parte=parte.strip()
        if parte[0:1]=="dd":
          fecha[0:1]=parte[3:4]
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
           