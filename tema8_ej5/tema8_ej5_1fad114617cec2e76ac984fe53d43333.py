class FechaHora:
    def __init__(self):
      self.d=0
      self.m=0
      self.a=0
      self.H=0
      self.M=0
      self.S=0
      f=""

    def __str__(self):
        return str(self.a)+"/"+str(self.m)+"/"+str(self.d)+" "+str(self.H)+":"+str(self.M)+":"+str(self.S)

    def fijarFecha(self,fecha):
      self.d=(fecha[0:2])
      self.m=(fecha[3:5])
      self.a=(fecha[6:])


    def fijarHora(self,fecha):
      self.H=(fecha[0:2])
      self.M=(fecha[3:5])
      self.S=(fecha[6:])
      

    def fijarFechaHora(self,fechahora):
      self.d=(fechahora[0:2])
      self.m=(fechahora[3:5])
      self.a=(fechahora[6:10])
      self.H=(fechahora[11:13])
      self.M=(fechahora[14:16])
      self.S=(fechahora[17:])
    

    def cambiar(self,parte):
        if parte[:4]=="aaaa":
            self.a=parte[7:]
        if parte[:2]=="mm":
            self.m=parte[3:]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           