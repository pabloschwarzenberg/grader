class FechaHora:
    def __init__(self):
        self.segundo=""
        self.minuto=""
        self.hora=""
        self.dia=""
        self.mes=""
        self.ano=""
    def __str__(self):
        r=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minuto+":"+self.segundo
        return r

    def fijarFecha(self,fecha):
        self.dia=fecha[0:2]
        self.mes=fecha[3:5]
        self.ano=fecha[6:8]
    def fijarHora(self,hora):
        self.hora=hora[0:2]
        self.minuto=hora[3:5]
        self.segundo=hora[6:8]
    def fijarFechaHora(self,fechahora):
        self.dia=fechahora[0:2]
        self.mes=fechahora[3:5]
        self.ano=fechahora[6:10]
        self.hora=fechahora[11:13]
        self.minuto=fechahora[14:16]
        self.segundo=fechahora[17:19]
    def cambiar(self,parte):
        parte=list(parte)
        print(parte)
        parametro=""
        valor=""
        for i in parte:
            if i.isalpha():
                parametro += i
            elif i.isdigit():
                valor += i
        if parametro=="SS":
            self.segundo=valor
        elif parametro=="MM":
            self.minuto=valor
        elif parametro=="HH":
            self.hora=valor
        elif parametro=="dd":
            self.dia=valor
        elif parametro=="mm":
            self.mes=valor
        elif parametro=="aaaa":
            self.ano=valor
            

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)