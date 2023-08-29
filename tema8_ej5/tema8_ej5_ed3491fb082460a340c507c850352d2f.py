class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""
        pass

    def __str__(self):
        return self.fecha[6:10]+"/"+self.fecha[3:5]+"/"+self.fecha[0:2]+" "+self.hora

    def fijarFecha(self,fecha):
        self.fecha = fecha
        pass

    def fijarHora(self,hora):
        self.hora = hora  
        pass

    def fijarFechaHora(self,fechahora):
        self.fecha = fechahora[0:11]
        self.hora = fechahora[11:]        
        pass

    def cambiar(self,parte):
        linea = parte.split("=")
        a = self.fecha.split("-")
        b = self.hora.split(":")

        if linea[0] == "dd":
           a[0] = linea[1]
           self.fecha = "-".join(a)
        if linea[0] == "mm":
           a[1] = linea[1]
           self.fecha = "-".join(a)
        if linea[0].strip() == "aaaa":
           a[2] = linea[1].strip()
           self.fecha = "-".join(a)
        if linea[0] == "HH":
           b[0] = linea[1]
           self.hora = ":".join(a)
        if linea[0] == "MM":
           b[1] = linea[1]
           self.hora = ":".join(a)
        if linea[0] == "SS":
           b[2] = linea[1]
           self.hora = ":".join(a)
           


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

           