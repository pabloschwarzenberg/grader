class FechaHora:
    def __init__(self):
        self.hora=""
        self.fecha=""
        

    def __str__(self):
        return self.fecha, self.hora

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        lista=fechahora.split()
        self.fecha=lista[0]
        self.hora=lista[1]
        
    def cambiar(self,parte):
        parte.split("=")
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           