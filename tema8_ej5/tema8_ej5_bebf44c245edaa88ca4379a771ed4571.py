class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.fechahora=""

    def fijarFecha(self,fecha):
        self.fecha=fecha
        return self.fecha

    def fijarHora(self,hora):
        self.hora=hora
        return self.hora

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora[6:10]+"/"+fechahora[3:5]+"/"+fechahora[0:2]+fechahora[10:19]
        return self.fechahora

    def cambiar(self,parte):
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
           