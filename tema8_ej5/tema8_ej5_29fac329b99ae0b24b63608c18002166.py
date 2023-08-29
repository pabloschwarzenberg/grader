class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return self.aaaa + "/" + self.mm + "/" + self.dd + " " + self.HH + ":" + self.MM + ":" + self.SS

    def fijarFecha(self, fecha):
        lis_fecha = fecha.split("/")
        if len(lis_fecha) == 1:
            lis_fecha = lis_fecha[0].split("-")
        self.dd = lis_fecha[0]
        self.mm = lis_fecha[1]
        self.aaaa = lis_fecha[2]

    def fijarHora(self,hora):
        lis_hora = hora.split(":")
        self.HH = lis_hora[0]
        self.MM = lis_hora[1]
        self.SS = lis_hora[2]

    def fijarFechaHora(self,fechahora):
        fechahora_lis = fechahora.split(" ")
        fecha = fechahora_lis[0]
        hora = fechahora_lis[1]
        lis_hora = hora.split(":")
        lis_fecha = fecha.split("/")
        if len(lis_fecha) == 1:
            lis_fecha = lis_fecha[0].split("-")
        self.dd = lis_fecha[0]
        self.mm = lis_fecha[1]
        self.aaaa = lis_fecha[2]
        self.HH = lis_hora[0]
        self.MM = lis_hora[1]
        self.SS = lis_hora[2]

    def cambiar(self,parte):
        parte.replace(" ", "")
        parte_lis = parte.split("=")
        if parte_lis[0] == "dd":
            self.dd = parte_lis[1]
        if parte_lis[0] == "mm":
            self.mm = parte_lis[1]
        if parte_lis[0] == "aaaa":
            self.aaaa = parte_lis[1]
        if parte_lis[0] == "SS":
              self.SS = parte_lis[1]
        if parte_lis[0] == "MM":
            self.MM = parte_lis[1]
        if parte_lis[0] == "SS":
            self.SS = parte_lis[1]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    fh.cambiar("mm=10")
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)