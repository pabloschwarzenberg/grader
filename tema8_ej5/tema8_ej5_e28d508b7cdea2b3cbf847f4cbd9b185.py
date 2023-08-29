class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""
    def __str__(self):
        return str(self.fecha+self.hora)

    def fijarFecha(self, fecha):
        fecha1 = fecha[6:] + "/" + fecha[3:5] + "/" + fecha[:2]
        self.fecha = fecha1
        return self.fecha

    def fijarHora(self, hora):
        self.hora = " "+hora
        return self.hora

    def fijarFechaHora(self, fechahora):
        self.fecha= fechahora[6:10]+"/"+fechahora[3:5]+"/"+fechahora[0:2]
        self.hora=fechahora[10:]
        FH=str(self.fecha)+" "+str(self.hora)
        return FH

    def cambiar(self, parte):
        i = parte.find("=")
        e=parte.find(" ")
        if e!=-1:
            parametro=parte[:e]
            valor=parte[i+2:]
        else:
            parametro = parte[:i]
            valor = parte[i + 1:]
        if parametro=="dd":
            self.fecha=self.fecha[0:4]+"/"+self.fecha[5:7]+"/"+valor
        elif parametro=="mm":
            self.fecha = self.fecha[0:4] + "/" + valor + "/" + self.fecha[8:10]
        elif parametro=="aaaa":
            self.fecha = valor + "/" + self.fecha[5:7] + "/" + self.fecha[8:10]
        fechahora=self.fecha+self.hora

        return fechahora

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           