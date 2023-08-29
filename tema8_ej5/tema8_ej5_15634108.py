class FechaHora:
    def __init__(self):
        self.fecha="00-00-0000"
        self.hora="00:00"

    def __str__(self):
        lista_str1=self.fecha.split("-")
        lista_str2=self.fecha.split("-")
        lista_str1[0]=lista_str2[2]
        lista_str1[2]=lista_str2[0]
        fecha2="/".join(lista_str1)
        return str(fecha2)+" "+str(self.hora)

    def fijarFecha(self,fecha):
        self.fecha=fecha
        return self.fecha

    def fijarHora(self,hora):
        self.hora=hora
        return self.hora

    def fijarFechaHora(self,fechahora):
        lista_fecha=fechahora.split(" ")
        self.fecha=lista_fecha[0]
        self.hora=lista_fecha[1]
        return self.fecha,self.hora

    def  cambiar(self,parte):
        lista_parte=parte.split("=")
        lista_fecha=self.fecha.split("-")
        lista_hora=self.hora.split(":")
        if lista_parte[0]=="HH":
            lista_hora[0]=lista_parte[1]
            self.hora=":".join(lista_hora)
            return self.hora
        elif lista_parte[0]=="MM":
            lista_hora[1]=lista_parte[1]
            self.hora=":".join(lista_hora)
            return self.hora
        elif lista_parte[0]=="SS":
            lista_hora[2]=lista_parte[1]
            self.hora=":".join(lista_hora)
            return self.hora
        elif lista_parte[0]=="dd":
            lista_fecha[0]=lista_parte[1]
            self.fecha="-".join(lista_fecha)
            return self.fecha
        elif lista_parte[0]=="mm":
            lista_fecha[1]=lista_parte[1]
            self.fecha="-".join(lista_fecha)
            return self.fecha
        elif lista_parte[0]=="aaaa":
            lista_fecha[2]=lista_parte[1]
            self.fecha="-".join(lista_fecha)
            return self.fecha


if __name__ == "__main__":
    a=FechaHora()
    print(a)
    a.fijarFecha("30-04-1996")
    print(a)
    a.fijarHora("21:19:59")
    print(a)
    a.fijarFechaHora("04-02-1997 00:00:01")
    print(a)
    a.cambiar("aaaa=3456")
    print(a)
