class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""
    def __str__(self):
        return "/".join(self.fecha.replace("-","/").split("/")[::-1])+" "+self.hora

    def fijarFecha(self,fecha):
        self.fecha = fecha

    def fijarHora(self,hora):
        self.hora = hora

    def fijarFechaHora(self,fechahora):
        self.fecha = fechahora.split()[0]
        self.hora = fechahora.split()[1]

    def cambiar(self,parte):
        parte = parte.replace(" ","").split("=")
        sep = ""
        if "-" in self.fecha:
          sep = "-"
        else:
          sep = "/"
        fecha = self.fecha.split(sep)
        if parte[0]=="aaaa":
          fecha[2]=parte[1]
        elif parte[0]=="mm":
          fecha[1]=parte[1]
        elif parte[0]=="dd":
          fecha[0]=parte[1]
        self.fecha = sep.join(fecha)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           