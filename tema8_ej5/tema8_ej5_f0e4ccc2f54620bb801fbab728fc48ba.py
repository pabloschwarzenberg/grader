class FechaHora:
    def __init__(self):
        self.año = ""
        self.mes = ""
        self.dia = ""
        self.fecha = self.dia+"/"+self.mes+"/"+self.año
        self.hora = ""
        self.minuto = ""
        self.segundo = ""
        self.hora = self.hora+":"+self.minuto+"/"+self.segundo

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.año, self.mes, self.dia, self.hora, self.minuto, self.segundo)

    def fijarFecha(self,fecha):
        self.dia = fecha[:2]
        self.mes = fecha[3:5]
        self.año = fecha[7:]
        pass

    def fijarHora(self,hora):
        self.hora = hora[:2]
        self.minuto = hora[3:5]
        self.segundo = hora[7:]
        pass

    def fijarFechaHora(self,fechahora):
        datos = fechahora.split(" ")
        FechaHora.fijarFecha(self,datos[0])
        FechaHora.fijarHora(self,datos[1])
        pass

    def cambiar(self,parte):
        if parte[:2] == 'aa':
          self.año = parte.split("=")[1]
        elif parte[:2] == 'mm':
          self.mes = parte.split("=")[1]
        elif parte[:2] == 'dd':
          self.dia = parte.split("=")[1]
        elif parte[:2] == 'HH':
          self.hora = parte.split("=")[1]
        elif parte[:2] == 'MM':
          self.minuto = parte.split("=")[1]
        elif parte[:2] == 'SS':
          self.segundo = parte.split("=")[1]
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           