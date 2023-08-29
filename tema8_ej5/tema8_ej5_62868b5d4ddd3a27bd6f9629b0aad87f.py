class FechaHora:
    def __init__(self):
        self.dia="dd"
        self.mes="mm"
        self.año="aaaa"
        self.hora="HH"
        self.minuto="MM"
        self.segundo="SS"

    def __str__(self):
        string=self.año+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minuto+":"+self.segundo
        return string

    def fijarFecha(self,fecha):
        self.dia=fecha[:2]
        self.mes=fecha[3:5]
        self.año=fecha[6:]
    def fijarHora(self,hora):
        self.hora=hora[:2]
        self.minuto=hora[3:5]
        self.segundo=hora[6:]

    def fijarFechaHora(self,fechahora):
        self.dia=fechahora[:2]
        self.mes=fechahora[3:5]
        self.año=fechahora[6:10]
        self.hora=fechahora[11:13]
        self.minuto=fechahora[14:16]
        self.segundo=fechahora[17:]


    def cambiar(self,parte):
        parte=parte.replace(" ","")
        if parte.find("dd")!=-1:
          indice=parte.find("=")
          self.dia=parte[indice+1:]
        elif parte.find("mm")!=-1:
          indice=parte.find("=")
          self.mes=parte[indice+1:]
        elif parte.find("aaaa")!=-1:
          indice=parte.find("=")
          self.año=parte[indice+1:]
        elif parte.find("HH")!=-1:
          indice=parte.find("=")
          self.hora=parte[indice+1:]
        elif parte.find("MM")!=-1:
          indice=parte.find("=")
          self.minuto=parte[indice+1:]
        elif parte.find("SS")!=-1:
          indice=parte.find("=")
          self.segundo=parte[indice+1:]


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           