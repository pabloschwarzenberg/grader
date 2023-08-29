class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        

    def __str__(self):
        return "{0} {1}".format(self.fecha, self.hora)

    def fijarFecha(self,fecha):
        if fecha[2]=="-":
            fecha=fecha.split("-")
            fecha[0],fecha[2]=fecha[2],fecha[0]
            self.fecha="/".join(fecha)
        else:
            self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora
        

    def fijarFechaHora(self,fechahora):
        if fechahora[2]=="-":
            fecha=fechahora[0:10].split("-")
            fecha[0],fecha[2]=fecha[2],fecha[0]
            self.fecha="/".join(fecha)
        else:
            self.fecha=fechahora[0:10]
        self.hora=fechahora[11:]
        

    def cambiar(self,parte):
        fecha=self.fecha.split("/")
        numero=0
        for i in range(len(parte)):
            if parte[i].isdigit():
                numero=parte[i:]
                break
        if parte[0]=="d":
            fecha[2]=numero
        elif parte[0]=="m":
            fecha[1]=numero
        else:
            fecha[0]=numero
        self.fecha="/".join(fecha)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

