class FechaHora:
    def __init__(self):
        self.segundo = ""
        self.minuto = ""
        self.hora = ""
        self.dia = ""
        self.mes = ""
        self.ano = ""

    def __str__(self):
        s = self.ano+ "/" + self.mes + "/" + self.dia + " " + self.hora + ":" + self.minuto + ":" + self.segundo
        return s

    def fijarFecha(self, fecha):
        self.dia = fecha[0:2]
        self.mes = fecha[3:5]
        self.ano = fecha[6:]

    def fijarHora(self, hora):
        self.hora = hora[0:2]
        self.minuto = hora[3:5]
        self.segundo = hora[6:]
        pass


    def fijarFechaHora(self, fechahora):
        self.dia = fechahora[0:2]
        self.mes = fechahora[3:5]
        self.ano = fechahora[6:10]
        self.hora = fechahora[11:13]
        self.minuto = fechahora[14:16]
        self.segundo = fechahora[17:]

    def cambiar(self, parte):
        parte = parte.split(" ")
        parte = "".join(parte)
        print(parte)
        if parte[0:2] == "dd":
            if int(parte[3:]) < 1 or int(parte[3:]) > 31:
                return "NOPE"
            if 0 < int(parte[3:]) < 10:
                self.dia = "0" + parte[3]
            else:
                self.dia = parte[3:]
        if parte[0:2] == "mm":
            if int(parte[3:]) < 1 or int(parte[3:]) > 12:
                return "NOPE"
            if 0 < int(parte[3:]) < 10:
                self.mes = "0" + parte[3]
            else:
                self.mes = parte[3:]
        if parte[0:4] == "aaaa":
            self.ano = parte[5:]
        if parte[0:2] == "HH":
            if int(parte[3:]) < 0 or int(parte[3:]) > 24:
                return "NOPE"
            if 0 < int(parte[3:]) < 10:
                self.hora = "0" + parte[3]
            else:
                self.hora = parte[3:]
        if parte[3:] == "MM":
            if int(parte[3:]) < 0 or int(parte[3:]) > 60:
                return "NOPE"
            if 0 < int(parte[3:]) < 10:
                self.minuto = "0" + parte[3]
            else:
                self.minuto = parte[3:]
        if parte[3:] == "SS":
            if int(parte[3:]) < 0 or int(parte[3:]) > 60:
                return "NOPE"
            if 0 < int(parte[3:]) < 10:
                self.segundo = "0" + parte[3]
            else:
                self.segundo = parte[3:]
            pass






if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
