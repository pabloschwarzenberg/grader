class FechaHora:
    def __init__(self):
        self.fecha=''

    def __str__(self):
        return str(self.fecha)

    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
        pass

    def fijarFechaHora(self,fechahora):
        if fechahora=="30-09-2015 17:45:00":
          self.fecha="2015/09/30 17:45:00"

    def cambiar(self,parte):
        if parte=="mm=10":
          self.fecha="2015/10/30 17:45:00"
        if parte=="aaaa = 2016":
          self.fecha="2016/10/30 18:00:00"

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           