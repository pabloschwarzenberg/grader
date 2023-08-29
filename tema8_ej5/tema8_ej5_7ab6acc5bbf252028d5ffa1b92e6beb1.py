class FechaHora:
    def __init__(self):
        self.fecha="dd-mm-aaaa"
        self.hora="HH:MM:SS"
        self.FechaHora = "{0} {1}".format(self.fecha,self.hora)
        pass

    def __str__(self):
        return "{0}".format(self.FechaHora)

    def fijarFecha(self,fecha):
        self.fecha=fecha
        self.fecha=self.fecha[::-1]
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.fecha

    def fijarHora(self,hora):
        self.hora=hora
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.hora

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split()
        self.fecha=fechahora[0]
        self.fecha=self.fecha.split("-")
        self.fecha = self.fecha[::-1]
        self.fecha="/".join(self.fecha)
        self.fecha = self.fecha.replace("-", "/")
        self.hora=fechahora[1]
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.FechaHora

    def cambiar(self,parte):
        x=""
        for i in parte:
            if i==" ":
                x=x
            else:
                x=x+str(i)
            parte=x
        parte=parte.split("=")
        if parte[0]=="aaaa" or "dd" or "mm":
            self.fecha=self.fecha.split("/")
            if parte[0]=='aaaa':
                self.fecha[0]=parte[1]
            elif parte[0] == "dd":
                if int(parte[1])>31:
                    print("no se puede cambiar el dia por no ser valido")
                else:
                    self.fecha[2] = parte[1]
            elif parte[0] == "mm":
                if int(parte[1])>12:
                    print("no se puede cambiar el mes por no ser valido")
                else:
                    self.fecha[1] = parte[1]
        if parte[0]=="HH"or "MM" or "SS":
            self.hora=self.hora.split(":")
            if parte[0] == 'HH':
                if int(parte[1]) > 23:
                    print("no se puede cambiar la hora por no ser valido")
                else:
                    self.hora[0] = parte[1]
            elif parte[0] == "MM":
                if int(parte[1]) > 59:
                    print("no se pueden cambiar los minutos por no ser valido")
                else:
                    self.hora[1] = parte[1]
            elif parte[0] == "SS":
                if int(parte[1]) > 59:
                    print("no se pueden cambiar los segundos por no ser valido")
                else:
                    self.hora[2] = parte[1]
        self.hora=":".join(self.hora)
        self.fecha="/".join(self.fecha)
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.fecha

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
    fh.cambiar("aaaa=    4000")
    fh.cambiar("dd   = 32")
    fh.cambiar("mm=13")
    print(fh)
    fh.cambiar("HH=24")
    fh.cambiar("HH=13")
    fh.cambiar("MM=56")
    fh.cambiar("SS=15")
    print(fh)

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split()
        self.fecha=fechahora[0]
        self.fecha=self.fecha.split("-")
        self.fecha = self.fecha[::-1]
        self.fecha="/".join(self.fecha)
        self.fecha = self.fecha.replace("-", "/")
        self.hora=fechahora[1]
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.FechaHora

    def cambiar(self,parte):
        x=""
        for i in parte:
            if i==" ":
                x=x
            else:
                x=x+str(i)
            parte=x
        parte=parte.split("=")
        if parte[0]=="aaaa" or "dd" or "mm":
            self.fecha=self.fecha.split("/")
            if parte[0]=='aaaa':
                self.fecha[0]=parte[1]
            elif parte[0] == "dd":
                self.fecha[2] = parte[1]
            elif parte[0] == "mm":
                self.fecha[1] = parte[1]
        self.fecha="/".join(self.fecha)
        self.FechaHora = "{0} {1}".format(self.fecha, self.hora)
        return self.fecha

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)


