class FechaHora:
    def __init__(self):
      self.dia = 00
      self.mes = 00
      self.ano = 0000
      #
      self.hora = 00
      self.minuto = 00
      self.seg = 00
    def fijarFecha(self,fecha):
      if "/" in fecha:
        f = fecha.split("/")
        for x in range(len(f)):
          if x == 0:
            self.dia = f[x]
          elif x == 1:
            self.mes = f[x]
          elif x == 2:
            self.ano = f[x]
      else:
        f = fecha.split("-")
        for x in range(len(f)):
          if x == 0:
            self.dia = f[x]
          elif x == 1:
            self.mes = f[x]
          elif x == 2:
            self.ano = f[x]
    def fijarHora(self,hora):
      f = hora.split(":")
      for x in range(len(f)):
        if x == 0:
          self.hora = f[x]
        elif x == 1:
          self.minuto = f[x]
        elif x == 2:
          self.seg = f[x]

    def fijarFechaHora(self,fechahora):
      f = fechahora.split(" ")
      if "/" in f[0]:
        f1 = f[0].split("/")
        for x in range(len(f1)):
          if x == 0:
            self.dia = f1[x]
          elif x == 1:
            self.mes = f1[x]
          elif x == 2:
            self.ano = f1[x]
      else:
        f1 = f[0].split("-")
        for x in range(len(f1)):
          if x == 0:
            self.dia = f1[x]
          elif x == 1:
            self.mes = f1[x]
          elif x == 2:
            self.ano = f1[x]
            
      f2 = f[1].split(":")
      for x in range(len(f2)):
        if x == 0:
          self.hora = f2[x]
        elif x == 1:
          self.minuto = f2[x]
        elif x == 2:
          self.seg = f2[x]

    def cambiar(self,parte):
      f = parte.split("=")
      f[0].replace(" ", "")
      f[0].strip()
      f[1].replace(" ", "")
      f[1].strip()
      if f[0] == 'dd':
        self.dia = int(f[1])
      elif f[0] == 'mm':
        self.mes = int(f[1])
      elif f[0] == 'aaaa' or f[0] == 'aaaa ' or f[0] == ' aaaa':
        self.ano = int(f[1])
      elif f[0] == 'HH':
        self.hora = int(f[1])
      elif f[0] == 'MM':
        self.minuto = int(f[1])
      elif f[0] == 'SS':
        self.seg = int(f[1])
        
    def __str__(self):
      return str(self.ano)+'/'+str(self.mes)+'/'+str(self.dia)+' '+str(self.hora)+':'+str(self.minuto)+':'+str(self.seg)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
