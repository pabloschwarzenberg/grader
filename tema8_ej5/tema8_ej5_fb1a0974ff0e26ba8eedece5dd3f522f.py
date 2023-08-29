class FechaHora:
    def __init__(self):
        self.dd = ""
        self.mm = ""
        self.aaaa = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""

    def fijarFecha(self,fecha):
        if "/" in fecha:
            lista = fecha.split("/")
            self.dd = lista[0]
            self.mm = lista[1]
            self.aaaa = lista[2]

        elif "-" in fecha:
            lista = fecha.split("-")
            self.dd = lista[0]
            self.mm = lista[1]
            self.aaaa = lista[2]

    def fijarHora(self,hora):
        lista = hora.split(":")
        self.HH = lista[0]
        self.MM = lista[1]
        self.SS = lista[2]

    def fijarFechaHora(self,info):
        lista = info.split(" ")
        self.fijarFecha(lista[0])
        self.fijarHora(lista[1])

    def cambiar(self,cambio):
        cambio = cambio.strip().split("=")
        if "dd" == cambio[0].strip():
            self.dd = cambio[1].strip()

        elif "mm" == cambio[0].strip():
            self.mm = cambio[1].strip()

        elif "aaaa" == cambio[0].strip():
            self.aaaa = cambio[1].strip()

        elif "HH" == cambio[0].strip():
            self.HH = cambio[1].strip()

        elif "MM" == cambio[0].strip():
            self.MM = cambio[1].strip()

        elif "SS" == cambio[0].strip():
            self.SS = cambio[1].strip()

    def __str__(self):
        return str(self.aaaa)+"/"+str(self.mm)+"/"+str(self.dd)+" "+str(self.HH)+":"+str(self.MM)+":"+str(self.SS)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           