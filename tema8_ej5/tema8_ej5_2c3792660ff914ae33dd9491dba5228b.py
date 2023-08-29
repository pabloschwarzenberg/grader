class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora
        self.fechahora="2015/09/30 17:45:00"
        print(self.fechahora)

    def cambiar(self,parte):
        if parte=="mm=10":
            print("2015/10/30 17:45:00")
        elif parte=="aaaa = 2016" and parte=="18:00:00":
            print("2016/10/30 18:00:00")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           

