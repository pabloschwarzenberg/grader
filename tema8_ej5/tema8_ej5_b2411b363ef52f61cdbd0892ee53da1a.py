class FechaHora:
    def __init__(self):
      self.ano=''
      self.mes=''
      self.dia=''
      self.hora=''
      self.minuto=''
      self.segundo=''
    def __str__(self):
        return self.ano+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minuto+":"+self.segundo
    def fijarFecha(self,fecha):
        if "/" in fecha:
          fecha=fecha.split("/")
        if "-" in fecha:
          fecha=fecha.split("-")
        self.dia=fecha[0]
        self.mes=fecha[1]
        self.ano=fecha[2]
    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hora=hora[0]
        self.minuto=hora[1]
        self.segundo=hora[2]
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fechahora[0]=fechahora[0].split("/")
        fechahora[1]=fechahora[1].split(":")
        self.dia=fechahora[0][0]
        self.mes=fechahora[0][1]
        self.ano=fechahora[0][2]
        self.hora=fechahora[1][0]
        self.minuto=fechahora[1][1]
        self.segundo=fechahora[1][2]
        
    def cambiar(self,parte):
      cosa=parte.split("=")
      if cosa[0]=='dd':
        self.dia=cosa[1]
      elif cosa[0]=='mm':
        self.mes=(cosa[1])
      elif cosa[0]=='aa':
        self.ano=(cosa[1])
      elif cosa[0]=='HH':
        self.hora=(cosa[1])
      elif cosa[0]=='MM':
        self.minuto=(cosa[1])
      elif cosa[0]=='SS':
        self.segundo=cosa[1]
