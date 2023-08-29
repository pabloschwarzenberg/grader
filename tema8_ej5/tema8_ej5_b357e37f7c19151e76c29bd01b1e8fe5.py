class FechaHora:
    def __init__(self):
        self.dia=""
        self.mes=""
        self.ano=""
        self.horas=""
        self.minuto=""
        self.segundo=""
        self.fecha=""
        self.hora=""
        pass

    def __str__(self):
        return self.fecha+" "+self.hora

    def fijarFecha(self,fecha):
        listaf=list(fecha)
        dia=str(listaf[0])+str(listaf[1])
        self.dia=dia
        mes=str(listaf[3])+str(listaf[4])
        self.mes=mes
        ano=str(listaf[6])+str(listaf[7])+str(listaf[8])+str(listaf[9])
        self.ano=ano
        self.fecha=ano+"/"+mes+"/"+dia

    def fijarHora(self,hora):
        listah=list(hora)
        hora=str(listah[0])+str(listah[1])
        self.horas=hora
        minuto=str(listah[3])+str(listah[4])
        self.minuto=minuto
        segundo=str(listah[6])+str(listah[7])
        self.segundo=segundo
        self.hora=hora+":"+minuto+":"+segundo

    def fijarFechaHora(self,fechahora):
        listafh=list(fechahora)
        dia=str(listafh[0])+str(listafh[1])
        self.dia=dia
        mes=str(listafh[3])+str(listafh[4])
        self.mes=mes
        ano=str(listafh[6])+str(listafh[7])+str(listafh[8])+str(listafh[9])
        self.ano=ano

        hora=str(listafh[11])+str(listafh[12])
        self.horas=hora
        minuto=str(listafh[14])+str(listafh[15])
        self.minuto=minuto
        segundo=str(listafh[17])+str(listafh[18])
        self.segundo=segundo
        self.fecha=ano+"/"+mes+"/"+dia
        self.hora=hora+":"+minuto+":"+segundo

    def cambiar(self,parte):
        parte=parte.replace(" ", "")
        listap=list(parte)
        parametro=str(listap[0])+str(listap[1])
        if (parametro=="dd"):
            dia=str(listap[3])+str(listap[4])
            self.dia=dia
        
        if (parametro=="mm"):
            mes=str(listap[3])+str(listap[4])
            self.mes=mes

        if (parametro=="aa"):
            ano=str(listap[5])+str(listap[6])+str(listap[7])+str(listap[8])
            self.ano=ano

        if (parametro=="HH"):
            hora=str(listap[3])+str(listap[4])
            self.horas=hora

        if (parametro=="MM"):
            minuto=str(listap[3])+str(listap[4])
            self.minuto=minuto

        if (parametro=="SS"):
            segundo=str(listap[3])+str(listap[4])
            self.segundo=segundo
        self.fecha=self.ano+"/"+self.mes+"/"+self.dia
        self.hora=self.horas+":"+self.minuto+":"+self.segundo

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           