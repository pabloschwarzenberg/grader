class FechaHora:
    def __init__(self):
        pass


    def __str__(self):
        a= self.ano+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minutos+":"+self.segundos
        return a
    def fijarFecha(self,fecha):
        Fecha=fecha.split("/")
        if len(Fecha)!=1:
            self.dia=Fecha[1]
            self.mes=Fecha[0]
            self.ano=Fecha[2]
        else:
            Fecha=fecha.split("-")
            self.dia=Fecha[0]
            self.mes=Fecha[1]
            self.ano=Fecha[2]

    def fijarHora(self,hora):
        Hora=hora.split(":")
        self.segundos=Hora[2]
        self.minutos=Hora[1]
        self.hora=Hora[0]

    def fijarFechaHora(self,fechahora):
        fecha_y_hora=fechahora.split(" ")
        fecha=fecha_y_hora[0]
        Fecha=fecha.split("/")
        if len(Fecha)!=1:
            self.dia=Fecha[1]
            self.mes=Fecha[0]
            self.ano=Fecha[2]
        else:
            Fecha=fecha.split("-")
            self.dia=Fecha[0]
            self.mes=Fecha[1]
            self.ano=Fecha[2]
        hora=fecha_y_hora[1]
        Hora=hora.split(":")
        self.segundos=Hora[2]
        self.minutos=Hora[1]
        self.hora=Hora[0]
    def cambiar(self,parte):
        parte=parte.split("=")

        if parte[0]=="mm":
            self.mes=parte[1]
        elif parte[0]=="dd":
            self.dis=parte[1]
        elif parte[0]=="HH":
            self.hora=parte[1]
        elif parte[0]=="MM":
            self.minutos=parte[1]
        elif parte[0]=="SS":
            self.segundos=parte[1]
        else:
            self.ano=(parte[1].strip(" "))

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           