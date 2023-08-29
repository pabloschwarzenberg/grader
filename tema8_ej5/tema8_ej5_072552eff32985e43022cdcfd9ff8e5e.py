class FechaHora:
    def __init__(self):
        self.ano=""
        self.mes=""
        self.dia=""
        self.horas=""
        self.minuto=""
        self.segundo=""

    def __str__(self):
        return self.ano+"/"+self.mes+"/"+self.dia+" "+self.horas+":"+self.minuto+":"+self.segundo

    def fijarFecha(self,fecha):
        dia=fecha[0]+fecha[1]
        mes=fecha[3]+fecha[4]
        ano=fecha[6]+fecha[7]+fecha[8]+fecha[9]

    def fijarHora(self,hora):
        horas=hora[1]+hora[2]
        minuto=hora[4]+hora[5]
        segundo=hora[7]+hora[8]

    def fijarFechaHora(self,fechahora):
        dia=fechahora[1]+fechahora[2]
        mes=fechahora[4]+fechahora[5]
        ano=fechahora[7]+fechahora[8]+fechahora[9]+fechahora[10]
        horas=fechahora[12]+fechahora[13]
        minuto=fechahora[15]+fechahora[16]
        segundo="00"

    def cambiar(self,parte):
        if parte[1]=="d":
            if len(parte)==6:
                dia=parte[3]
            elif len(parte)==7:
                dia=parte[3]+parte[4]
        elif parte[1]=="m":
            if len(parte)==6:
                mes=parte[3]
            elif len(parte)==7:
                mes=parte[3]+parte[4]
        elif parte[1]=="a":
            ano=parte[3]+parte[4]+parte[5]+parte[6]
        elif parte[1]=="H":
            pass
        elif parte[1]=="M":
            pass
        elif parte[1]=="S":
            pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           