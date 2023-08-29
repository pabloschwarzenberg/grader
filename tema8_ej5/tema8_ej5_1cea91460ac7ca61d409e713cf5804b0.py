class FechaHora:
    def __init__(self):
        self.dia=0
        self.mes=0
        self.ano=0
        self.hora=0
        self.minuto=0
        self.segundo=0

    def __str__(self):
      if len(str(self.mes))<2: self.mes="0"+str(self.mes)
      if len(str(self.dia))<2: self.dia="0"+str(self.dia)
      if len(str(self.hora))<2: self.hora="0"+str(self.hora)
      if len(str(self.minuto))<2: self.minuto="0"+str(self.minuto)
      if len(str(self.segundo))<2: self.segundo="0"+str(self.segundo)      
      return "{}/{}/{} {}:{}:{}".format(self.ano,self.mes,self.dia,self.hora,self.minuto,self.segundo)

    def fijarFecha(self,fecha):
      if len(fecha.split("/"))==3: list_fecha=fecha.split("/")
      else: list_fecha=fecha.split("-")
      self.ano=int(list_fecha[2])
      self.mes=int(list_fecha[1])
      self.dia=int(list_fecha[0])

    def fijarHora(self,hora):
      list_hora=hora.split(":")
      self.hora=int(list_hora[0])
      self.minuto=int(list_hora[1])
      self.segundo=int(list_hora[2])

    def fijarFechaHora(self,fechahora):
      list_total=fechahora.split()
      self.fijarFecha(list_total[0])
      self.fijarHora(list_total[1])
      
    def cambiar(self,parte):
        partel=parte.split("=")
        if partel[0].strip()=="aaaa": self.ano=int(partel[1].strip())
        elif partel[0]=="dd": self.dia=int(partel[1])
        elif partel[0]=="mm": self.mes=int(partel[1])
        elif partel[0]=="HH": self.hora=int(partel[1])
        elif partel[0]=="MM": self.minuto=int(partel[1])
        elif partel[0]=="SS": self.segundo=int(partel[1])

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
