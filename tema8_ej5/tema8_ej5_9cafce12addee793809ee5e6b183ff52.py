class FechaHora:
    def __init__(self):
        self.fechactual=[]
        self.horactual=[]
        pass

    def __str__(self):
        c=[]
        a='/'.join(self.fechactual.reverse())
        c.append(a)
        b=':'.join(self.horactual)
        c.append(b)
        z=' '.join(c)
        return z
      

    def fijarFecha(self,fecha):
        hola=fecha.split("/")
        d=''.join(hola)
        hola1=d.split('-')
        self.fechactual=hola1
        
    def fijarHora(self,hora):
        hola=hora.split(":")
        self.horactual=hola
  

    def fijarFechaHora(self,fechahora):
        hola=fechahora.split(" ")
        hola1=hola[1]
        hola3=hola1.split(":")
        self.horactual=hola3
        hola2=hola[0]
        hola4=hola2.split("/")
        d=''.join(hola4)
        hola5=d.split('-')
        self.fechactual=hola5
        pass

    def cambiar(self,parte):
        parto=parte.split("=")
        if parto[0]=="dd":
            self.fechactual[0]=parto[1]
        elif parto[0]=="mm":
            self.fechactual[1]=parto[1]
        elif parto[0]=="aaaa":
            self.fechactual[2]=parto[1]
        elif parto[0]=="HH":
            self.horactual[0]=parto[1]
        elif parto[0]=="MM":
            self.horactual[1]=parto[1]
        elif parto[0]=="SS":
            self.horactual[2]=parto[1]
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           