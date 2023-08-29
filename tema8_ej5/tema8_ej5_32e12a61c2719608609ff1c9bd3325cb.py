class FechaHora:
    def __init__(self):
        self.fechahora=[]

    def __str__(self):
        
        return "{0}".format("".join(self.fechahora))

    def fijarFecha(self,fecha):
        self.fechahora[0][0]=fecha
        return self.fechahora

    def fijarHora(self,hora):
        
        self.fechahora[0]=self.fechahora[0][:11]+hora
        return "".join(self.fechahora)

    def fijarFechaHora(self,fechahora):
        self.fechahora.append(fechahora)
        x=self.fechahora[0][0:2]
        y=self.fechahora[0][6:10]
        
        self.fechahora[0]=y+self.fechahora[0][2:]
        
        self.fechahora[0]=self.fechahora[0][:8]+x+self.fechahora[0][12:]
        self.fechahora[0]=self.fechahora[0][:4]+"/"+self.fechahora[0][5:7]+"/"+self.fechahora[0][8:]
        
        
        return self.fechahora

    def cambiar(self,parte):
       
        if parte[0]=="d":
         self.fechahora[0]=parte[3:]+self.fechahora[0][2:]
        if parte[0]=="m":
          
          self.fechahora[0]=self.fechahora[0][0:5]+parte[3:]+self.fechahora[0][7:]
        if parte[0]=="a":
          self.fechahora[0]=parte[7:]+self.fechahora[0][4:]
        if parte[0]=="0" or parte[0]=="1" or parte[0]=="2":
          self.fechahora[1]=parte
        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           