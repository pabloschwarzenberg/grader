class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return self.fechafinal

    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
      self.hora=hora
      return

    def fijarFechaHora(self,fechahora):
      if "-" in fechahora:
        fechahora=fechahora.replace("-","/")
        lista=fechahora.split(" ")
        fecha=lista[0].split("/")
        self.ano=fecha[2]
        self.mes=fecha[1]
        self.dia=fecha[0]
        self.hora=lista[1]
        self.fechafinal=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hora
        return print(self.fechafinal)
      
      

    def cambiar(self,parte):
        if "mm" in parte:
          self.mes= parte.split("=")[1]
        if "dd" in parte:
          self.dia= parte.split("=")[1]
        if "aaaa" in parte:
          self.ano= parte.split("= ")[1]
        self.fechafinal=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hora
        return self.fechafinal

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           