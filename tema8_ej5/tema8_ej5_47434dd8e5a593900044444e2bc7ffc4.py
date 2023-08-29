class FechaHora:
    def __init__(self):
        self.dd = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""
        self.mm = ""
        self.aaaa = ""

    def fijarFecha(self, fecha):
        lista_fecha = fecha.split(fecha[2])
        self.dd = lista_fecha[0]
        self.mm = lista_fecha[1]
        self.aaaa = lista_fecha[2]

    def fijarHora(self, hora):
        lista_hora = hora.split(":")
        self.HH = lista_hora[0]
        self.MM = lista_hora[1]
        self.SS = lista_hora[2]

    def fijarFechaHora(self, fechahora):
        lista_fechahora = fechahora.split()
        fecha = lista_fechahora[0]
        hora = lista_fechahora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, cambio):
        lista_c = cambio.split("=")
        lista_cambio = [lista_c[0].strip(),lista_c[1].strip()]
        if self.rango(lista_cambio[0],lista_cambio[1]) == True:
            if lista_cambio [0] == "aaaa":
                self.aaaa = lista_cambio[1]
            elif lista_cambio [0] == "mm":
                self.mm = lista_cambio[1]
            elif lista_cambio [0] == "SS":
                self.SS = lista_cambio[1]
            elif lista_cambio [0] == "MM":
                self.MM = lista_cambio[1]
            elif lista_cambio [0] == "HH":
                self.HH = lista_cambio[1]
            elif lista_cambio [0] == "dd":
                self.dd = lista_cambio[1]
        else:
            return("Lo siento, este cambio no se puede realizar")

    def rango(self, objeto, numero):
        if objeto == "dd" and  0 <= int(numero) <= 31:
            return True
        elif objeto == "HH" and 0 <= int(numero.lstrip("0")) <= 23:
            return True
        elif objeto == "MM" and 0 <= int(numero.lstrip("0")) <= 60:
            return True
        elif objeto == "SS" and 0 <= int(numero.lstrip("0")) <= 60:
            return True
        elif objeto == "mm" and 1 <= int(numero.lstrip("0")) <= 12:
            return True
        elif objeto == "aaaa":
            return True
        else:
            return False

    def __str__(self):
        return ("{0} {1}".format("{2}/{1}/{0}".format(self.dd,self.mm,self.aaaa),"{0}:{1}:{2}".format(self.HH,self.MM,self.SS)))

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           