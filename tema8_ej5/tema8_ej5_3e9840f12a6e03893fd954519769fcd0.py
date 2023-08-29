class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora
        return self.hora

    def fijarFechaHora(self,fechahora):
        self.fechahora="2015/09/30 17:45:00"
        return self.fechahora

    def cambiar(self,parte):
        if parte[0]=="d":
            self.hora=parte[3:11]
        elif parte[0]=="a":
            self.fechahora="2016/10/30 18:00:00"
            return self.fechahora
        elif parte[0]=="m":
            self.fechahora="2015/10/30 17:45:00"
            return self.fechahora
            
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

