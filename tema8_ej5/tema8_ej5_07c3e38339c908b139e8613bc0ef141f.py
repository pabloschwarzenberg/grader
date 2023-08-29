class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
      fechahora = self.fijarFechaHora
        return ""

    def fijarFecha(self,fecha):
      if "-" in fecha:
        fecha.replace("-","/")
      return fecha

    def fijarHora(self,hora):
      self
        pass

    def fijarFechaHora(self,fechahora):
        pass

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
           