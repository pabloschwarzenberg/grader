class FechaHora:
    def __init__(self):
        self.fecha = []
        self.hora = []
    def __str__(self):
        a = str(self.fecha[2])+"/"+str(self.fecha[1])+"/"+str(self.fecha[0])+" "+str(self.hora[0])+":"+str(self.hora[1])+":"+str(self.hora[2])
        return a
    def fijarFecha(self,fecha):
        a1 = False
        for i in fecha:
            if i == "/":
                a1= True
                break
        if a1 == True:
            b = fecha.split("/")
            self.fecha = b
        elif a1 == False:
            b = fecha.split("-")
            self.fecha = b
    def fijarHora(self, hora):
        a = hora.split(":")
        self.hora = a
    def fijarFechaHora(self,fechahora):
        a = fechahora.split(" ")
        a1 = False
        for i in a[0]:
            if i == "/":
                a1 = True
                break
        if a1 == True:
            b = a[0].split("/")
            self.fecha = b
        elif a1 == False:
            b = a[0].split("-")
            self.fecha = b
        a2 = a[1].split(":")
        self.hora = a2
    def cambiar(self,parte):
        b = "ddmmaaaa"
        c = "HHMMSS"
        d = parte.split("=")
        if " " in d[0]:
            d[0] = (d[0])[:-1]
        if " " in d[1]:
            d[1] = (d[1])[1:]
        if d[0] in b:
            if d[0] == "dd":
                self.fecha[0] = d[1]
            elif d[0] == "mm":
                self.fecha[1] = d[1]
            elif d[0] == "aaaa":
                self.fecha[2] = d[1]
        elif d[0] in c:
            if d[0] == "HH":
                self.hora[0] = d[1]
            elif d[0] == "MM":
                self.hora[1] = d[1]
            elif d[0] == "SS":
                self.hora[2] = d[1]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           