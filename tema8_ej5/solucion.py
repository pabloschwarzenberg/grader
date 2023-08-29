class FechaHora:
    def __init__(self):
        self.day=0
        self.month=0
        self.year=0
        self.hour=0
        self.minute=0
        self.second=0

    def __str__(self):
        s="{0:0>4}/{1:0>2}/{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}"
        return s.format(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second)

    def fijarFecha(self,fecha):
        if fecha.count("/")!=0:
            fecha=fecha.split("/")
        else:
            fecha=fecha.split("-")
        self.day=int(fecha[0])
        self.month=int(fecha[1])
        self.year=int(fecha[2])

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.hour=int(hora[0])
        self.minute=int(hora[1])
        self.second=int(hora[2])

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        if fechahora[0].count("/")!=0:
            fecha=fechahora[0].split("/")
        else:
            fecha=fechahora[0].split("-")
        hora=fechahora[1].split(":")
        self.day=int(fecha[0])
        self.month=int(fecha[1])
        self.year=int(fecha[2])
        self.hour=int(hora[0])
        self.minute=int(hora[1])
        self.second=int(hora[2])

    def cambiar(self,parte):
        parte=parte.lower().split("=")
        valor=int(parte[1])
        parte[0]=parte[0].strip(" ")
        if parte[0]=="dd":
            self.day=valor
        if parte[0]=="mm":
            self.month=valor
        if parte[0]=="aaaa":
            self.year=valor
        if parte[0]=="HH":
            self.hour=valor
        if parte[0]=="MM":
            self.minute=valor
        if parte[0]=="SS":
            self.second=valor

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)









