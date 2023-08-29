class FechaHora:
    def __init__(self):
        self.aaaa=""
        self.mm=""
        self.dd=""
        self.HH=""
        self.MM=""
        self.SS=""
        
    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(self.aaaa,self.mm,self.dd,self.HH,self.MM,self.SS)

    def fijarFecha(self,fecha):
        if fecha.find("/")!=-1:
            lista_fechas=fecha.split("/")
            self.aaaa=lista_fechas[2]
            self.mm=lista_fechas[1]
            self.dd=lista_fechas[0]
        elif fecha.find("-")!=-1:
            lista_fechas=fecha.split("-")
            self.aaaa=lista_fechas[2]
            self.mm=lista_fechas[1]
            self.dd=lista_fechas[0]

    def fijarHora(self,hora):
        lista_horas=hora.split(":")
        self.HH=lista_horas[0]
        self.MM=lista_horas[1]
        self.SS=lista_horas[2]

    def fijarFechaHora(self,fechahora):
        fechahora_separada=fechahora.split(" ")
        self.fijarHora(fechahora_separada[1])
        self.fijarFecha(fechahora_separada[0])

    def cambiar(self,parte):
        indice=parte.split("=")
        indice0=indice[0].strip(" ")
        indice1=indice[1][::-1]
        indice1=indice1.strip(" ")
        indice1=int(indice1[::-1])
        if indice0=="aaaa":
            self.aaaa=indice1
        elif indice0=="mm" and 0<indice1<13:
            self.mm=indice1
        elif indice0=="dd" and 0<indice1<32:
            self.dd=indice1
        elif indice0=="HH" and 0<=indice1<24:
            self.HH=indice1
        elif indice0=="MM" and 0<=indice1<60:
            self.MM=indice1
        elif indice0=="SS" and 0<=indice1<60:
            self.SS=indice1
        else:
            print("esa fecha/hora no existe")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)