class FechaHora:
    def __init__(self):
        self.fecha = "x"
        self.hora = "d"

    def __str__(self):
        return self.fecha + " " + self.hora

    def fijarFecha(self,fecha):
        if '-' in fecha:
            fecha = fecha.replace('-', '/')
        l_fecha = fecha.split('/')
        l_fecha.reverse()
        fecha = '/'.join(l_fecha)
        self.fecha = fecha

    def fijarHora(self,hora):
        self.hora = hora

    def fijarFechaHora(self,fechahora):
        fecha = fechahora.split()[0]
        hora = fechahora.split()[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,cambio):
        cambio = cambio.replace(" ", "")
        tipo = cambio.split("=")[0]
        dato = int(cambio.split("=")[1])
        l_fecha = self.fecha.split("/")
        l_hora = self.hora.split(":")

        if tipo == "aaaa":
            l_fecha[0] = str(dato)
        elif tipo == "mm" and 0 < dato < 13:
            l_fecha[1] = str(dato)
        elif tipo == "dd" and 0 < dato < 31:
            l_fecha[2] = str(dato)

        elif tipo == "HH" and 0 <= dato < 25:
            l_hora[0] = str(dato)
        elif tipo == "MM" and 0 <= dato < 60:
            l_hora[1] = str(dato)
        elif tipo == "SS" and 0 <= dato < 60:
            l_hora[2] = str(dato)
        else:
            return "No se puede"

        self.fecha = '/'.join(l_fecha)
        self.hora = ':'.join(l_hora)