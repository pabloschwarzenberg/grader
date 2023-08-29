class FechaHora:
    def __init__(self):
      self.hora=""
      self.fecha=""
      pass
    def __str__(self):
      self.fecha=self.fecha.split("/")
      return ""

    def fijarFecha(self,fecha):
      self.fecha=fecha
      
    def fijarHora(self,hora):
      self.hora=hora
  

    def fijarFechaHora(self,fechahora):
      lista=fechahora.split(" ")
      self.fecha=lista[0]
      self.hora=lista[1]

    def cambiar(self,parte):
        if parte==mm:
          self.fecha=fecha.split("/")
          self.fecha=fecha.split("-")
          fecha[i].replace(mm)
      

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           