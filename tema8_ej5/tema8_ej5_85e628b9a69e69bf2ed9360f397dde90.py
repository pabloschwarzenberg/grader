class FechaHora:
    def __init__(self):
        self.ano=0
        self.mes=0
        self.dia=0
        self.hora=0
        self.minu=0
        self.seg=0

    def __str__(self):
        fecha=self.ano+"/"+self.mes+"/"+self.dia
        tiempo=self.hora+":"+self.minu+":"+self.seg
        return fecha+" "+tiempo

    def fijarFecha(self,fecha):
        if "-" in fecha:
            fecha=fecha.split("-")
            self.ano=fecha[2]
            self.mes=fecha[1]
            self.dia=fecha[0]
        else:
            fecha=fecha.split("/")
            self.ano=fecha[2]
            self.mes=fecha[1]
            self.dia=fecha[0]
            
    def fijarHora(self,hora):
        tiempo=hora.split(":")
        self.hora=tiempo[0]
        self.minu=tiempo[1]
        self.seg=tiempo[2]

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fecha=fechahora[0]
        hora=fechahora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)
        
    def cambiar(self,parte):
        parte=parte.split("=")
        tipo=parte[0].strip(" ")
        cambio=parte[1].strip(" ")
        if tipo=="aaaa":
            self.ano=cambio
        elif tipo=="mm":
            self.mes=cambio
        elif tipo=="dd":
            self.dia=cambio
        elif tipo=="HH":
            self.hora=cambio
        elif tipo=="MM":
            self.minu=cambio
        elif tipo=="SS":
            self.seg=cambio
        else:
            print("Parametro de cambio no válido")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           