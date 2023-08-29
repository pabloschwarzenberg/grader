class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.FechaHora=""

    def __str__(self):
        return "{}" "{}".format(self.fecha,self.hora)
        

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        self.FechaHora=fechahora

    def cambiar(self,parte):
        cambiar=cambiar.strip()
        cambiar=cambiar.split("=")
        for numero in cambiar:
            if numero[1]!= False:
              self.dia=numero[1]
        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           