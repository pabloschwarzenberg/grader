class FechaHora:
    def __init__(self):
        self.hora = ""
        self.fecha = ""

    def __str__(self):
        return self.fecha + " " + self.hora

    def fijarFecha(self,fecha):
        self.fecha = fecha[6:] + "/" + fecha[3:5] + "/" + fecha[0:2]

    def fijarHora(self,hora):
        self.hora = hora

    def fijarFechaHora(self,fechahora):
        self.fecha = fechahora[6:10] + "/" + fechahora[3:5] + "/" + fechahora[0:2]
        print("fh f:",self.fecha)
        self.hora = fechahora[11:]
        print("fh h:",self.hora)

    def cambiar(self,parte):
        l = parte.split("=")
        if l[0] == "dd":
            self.fecha = self.fecha[0:8] + l[1]
        elif l[0] == "mm":
            self.fecha = self.fecha[0:5] + l[1] + self.fecha[7:]
        elif str.strip(l[0]) == "aaaa":
            self.fecha = str.strip(l[1]) + self.fecha[4:]
        elif l[0] == "HH":
            pass
        elif l[0] == "MM":
            pass
        elif l[0] == "SS":
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
   