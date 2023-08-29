class FechaHora:
    def __init__(self):
        self.dia=0
        self.mes=0
        self.año=0
        self.hora=0
        self.minuto=0
        self.segundo=0


    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(self.año,self.mes,self.dia,self.hora,self.minuto,self.segundo)

    def fijarFecha(self,fecha):
        f=fecha.split("-")
        self.dia=f[0]
        self.mes=f[1]
        self.año=f[2]       

    def fijarHora(self,hora):
        h=hora.split(":")
        self.hora=h[0]
        self.minuto=h[1]
        self.segundo=h[2]


    def fijarFechaHora(self,fechahora):
        fh=fechahora.split(" ")
        f=fh[0]
        h=fh[1]
        fecha=f.split("-")
        hora=h.split(":")
        self.dia=fecha[0]
        self.mes=fecha[1]
        self.año=fecha[2]
        self.hora=hora[0]
        self.minuto=hora[1]
        self.segundo=hora[2]

    def cambiar(self,parte):
        p=parte.split("=")
        atributo=p[0]
        valor=p[1]
        if atributo == "mm":
            self.mes = valor
        elif atributo == "dd":
            self.dia = valor 
        elif atributo == "MM":
            self.minuto = valor
        elif atributo == "HH":
            self.hora = valor
        elif atributo == "SS":
            self.segundo = valor
        elif atributo.strip() == "aaaa":
            self.año = valor.split(" ")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

