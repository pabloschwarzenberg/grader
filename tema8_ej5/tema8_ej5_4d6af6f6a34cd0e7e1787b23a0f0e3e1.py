class FechaHora:
    def __init__(self):
      pass

    def __str__(self):
        string=self.f[2]+"/"+self.f[1]+"/"+self.f[0]+" "+ self.h[0]+":"+self.h[1]+":"+self.h[2]
        return string

    def fijarFecha(self,fecha):
        if "/" in fecha:
            self.f=fecha.split("/")
        elif "-" in fecha:
            self.f=fecha.split("-")
        return self
        

    def fijarHora(self,hora):
        self.h=hora.split(":")

        
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        self.f=fechahora[0].split("-")
        self.h=fechahora[1].split(":")
    

    def cambiar(self,parte):
        if "dd" in parte:
            self.f[0]=parte[3:]
        if "mm" in parte:
            self.f[1]=parte[3:]
        if "aaaa" in parte:
            self.f[2]=parte[7:]
        if "HH" in parte:
            self.h[0]=parte[3:]
        if "MM" in parte:
            self.h[1]=parte[3:]
        if "SS" in parte:
            self.h[2]=parte[3:]


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    fh.cambiar("mm=10")
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")