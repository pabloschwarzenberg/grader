class FechaHora:
    def __init__(self):
        self.fecha = ["aaaa","mm","dd"]
        self.hora = ["HH","MM","SS"]
        
    def __str__(self):
        fecha = self.fecha
        hora = self.hora
        return "/".join(fecha) + " " + ":".join(hora)

    def fijarFecha(self,fecha):
        if "-" in fecha:
            fecha = fecha.split("-")
            fecha.reverse()
            self.fecha = fecha
        elif "/" in fecha:
            fecha = fecha.split("/")
            fecha.reverse
            self.fecha = fecha

    def fijarHora(self,hora):
        self.hora = hora.split(":")

    def fijarFechaHora(self,fechahora):
        fechahora = fechahora.split(" ")
        self.hora = fechahora[1].split(":")
        if "-" in fechahora[0]:
            fecha = fechahora[0].split("-")
            fecha.reverse()
            self.fecha = fecha
        if "/" in fechahora[0]:
            fecha = fechahora[0].split("/")
            fecha.reverse()
            self.fecha = fecha

    def cambiar(self,parte):
        fecha = self.fecha
        hora = self.hora
        if parte[0] == "a":
            parte = parte.split(" = ")
        else:
            parte = parte.split("=")
        print(parte)
        unidad = parte[0]
        numero = parte[1]
        dic = {"aaaa":0,"mm":1,"dd":2,"HH":0,"MM":1,"SS":2}
        if unidad == "dd" or unidad == "aaaa" or unidad == "mm":
            fecha[dic[unidad]] = numero
            self.fecha = fecha
        if unidad == "HH" or unidad == "MM" or unidad == "SS":
            hora[dic[unidad]] = numero
            self.hora = hora