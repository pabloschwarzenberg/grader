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
    def fijarFechaHora(self,fh):
        self.fecha = fh[6:10] + "/" + fh[3:5] + "/" + fh[0:2]
        self.hora = fh[10:]
        HF = str(self.fecha)+" "+str(self.hora)
        return HF
    def cambiar(self,parte):
        i =parte.find("=")
        e = parte.find(" ")
        if e!=-1:
            p = parte[:e]
            valor=parte[i+2:]
        else:
            p = parte[:i]
            valor = parte[i + 1:]
        if p == "dd":
            self.fecha=self.fecha[0:4] + "/" + self.fecha[5:7] + self.fecha[3:5] + "/" + self.fecha[:2]
        elif p == "mm":
            self.fecha = self.fecha[0:4] + "/" + valor + self.fecha[3:5] + "/" + self.fecha[:2]
        elif p == "aaaa":
            self.fecha = valor + "/" + self.fecha[5:7]  + self.fecha[3:5] + "/" + self.fecha[:2]
        fh = self.fecha+self.hora

        return fh

    if __name__ == "__main__":
        fh = FechaHora()
        fh.fijarFechaHora("30-09-2015 17:45:00")
        print(fh)