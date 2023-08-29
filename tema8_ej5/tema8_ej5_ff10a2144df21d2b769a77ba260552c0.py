class FechaHora:
    def __init__(self):
        self.hora=""
        self.fecha=""

    def __str__(self):
        lista=self.fecha.split("-")
        l=[]
        for i in lista:
            l.insert(0,i)
        kk="-".join(l)
        string="/".join(l)+" "+self.hora
        return string

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        fecha_y_hora=fechahora.split(" ")
        fecha=fecha_y_hora[0]
        hora=fecha_y_hora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)
        
    def cambiar(self,parte):
        lista_parte=list(parte)
        lista_fecha=self.fecha.split("-")
        lista_hora=self.hora.split(":")

        if lista_parte[0]=="m":
            string=lista_parte[3]+lista_parte[4]
            lista_fecha.insert(1,string)
            lista_fecha.pop(2)
            self.fecha="-".join(lista_fecha)
        
        if lista_parte[0]=="a":
            string=lista_parte[7]+lista_parte[8]+lista_parte[9]+lista_parte[10]
            lista_fecha.insert(2,string)
            lista_fecha.pop()
            self.fecha="-".join(lista_fecha)
        
    

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           

