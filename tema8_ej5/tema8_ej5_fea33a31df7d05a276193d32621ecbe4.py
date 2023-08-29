class FechaHora:
    def __init__(self):
       self.fecha="           "
       self.hora="          "
              
    def __str__(self):
        self.fecha=self.fecha[6:10]+"/"+self.fecha[3:5]+"/"+self.fecha[0:2]
        return self.fecha+" "+self.hora
        
    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        a=""
        for i in range(0,10):
           a=a+fechahora[i]
        h=""
        for i in range(11,19):
           h=h+fechahora[i]
        self.fecha=a
        self.hora=h
   
    def cambiar(self,parte):
        if "aaaa" in parte:
           ano=parte[-4:]
           self.fecha=self.fecha[:6]+ano
        if parte[:2]=="mm":
           mes=parte[-2:]
           self.fecha=self.fecha[:3]+mes+self.fecha[-5:]
        if "dd" in parte:
           dia=parte[-2:]
           fecha=dia+self.fecha[2:]
        
        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)


           