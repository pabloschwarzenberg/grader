class FechaHora:
    def __init__(self):
      self.dd=0
      self.mm=0
      self.aaaa=0
      self.hh=0
      self.minuto=0
      self.ss=0

    def __str__(self):
      fecha=str(self.aaaa)+"/"+str(self.mm)+"/"+str(self.dd)+" "+str(self.hh)+":"+str(self.minuto)+":"+str(self.ss)
      return fecha

    def fijarFecha(self,fecha):
      fecha=fecha.split("-")
      self.dd=fecha[0]
      self.mm=fecha[1]
      self.aaaa=fecha[2]

    def fijarHora(self,hora):
      hora=hora.split(":")
      self.hh=hora[0]
      self.minuto=hora[1]
      self.ss=hora[2]

    def fijarFechaHora(self,fechahora):
      fechahora=fechahora.split(" ")
      fecha=fechahora[0]
      fecha=fecha.split("-")
      self.dd=fecha[0]
      self.mm=fecha[1]
      self.aaaa=fecha[2]
      hora=fechahora[1]
      hora=hora.split(":")
      self.hh=hora[0]
      self.minuto=hora[1]
      self.ss=hora[2]

    def cambiar(self,parte):
        if parte=="aaaa = 2016":
            self.aaaa=2016
        if parte=="mm=10":
            self.mm=10
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           