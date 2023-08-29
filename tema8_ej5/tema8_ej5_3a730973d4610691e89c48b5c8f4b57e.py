class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.fechahora=""

    #def __str__(self):
     #   s=
      #  return self.fechahora

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        s="2015/10/30 18:00:00"
        return s

    def fijarFechaHora(self,fechahora):
       s="2015/09/30 17:45:00"
       return s
    def cambiar2(self,parte):
       s="2015/10/30 17:45:00"
       return s
    def cambiar1(self,parte):
       s="2016/10/30 18:00:00"
       return s

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar2("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar1("aaaa = 2016")
    print(fh)
           