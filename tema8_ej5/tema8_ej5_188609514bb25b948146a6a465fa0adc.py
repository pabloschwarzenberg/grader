class FechaHora:
    def __init__(self):
        self.hora = ""
        self.minuto = ""
        self.segundo = ""
        self.dia = ""
        self.mes = ""
        self.año = ""

    def fijarFecha(self,fecha):
        lista_fecha = []
        if "/" in fecha:
            lista_fecha = fecha.split("/")
        else:
            lista_fecha = fecha.split("-")
        self.dia = lista_fecha[0]
        self.mes = lista_fecha[1]
        self.año = lista_fecha[2]

    def fijarHora(self,hora):
        lista_hora = hora.split(":")
        self.hora = lista_hora[0]
        self.minuto = lista_hora[1]
        self.segundo = lista_hora[2]

    def fijarFechaHora(self,fechahora):
        lista_fechahora = fechahora.split()
        self.fijarFecha(lista_fechahora[0])
        self.fijarHora(lista_fechahora[1])

    def cambiar(self,parte):
        parte = parte.replace(" ", "")
        lista_parte = parte.split("=")
        valor = lista_parte[1]
        if lista_parte[0][0] == "d":
            self.dia = valor
        elif lista_parte[0][0] == "m":
            self.mes = valor
        elif lista_parte[0][0] == "a":
            self.año = valor
        elif lista_parte[0][0] == "H":
            self.hora = valor
        elif lista_parte[0][0] == "M":
            self.minuto = valor
        elif lista_parte[0][0] == "S":
            self.segundo = valor

    def __str__(self):
        return self.año + "/" + self.mes + "/" + self.dia + " " + self.hora + ":" + self.minuto + ":" + self.segundo


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           