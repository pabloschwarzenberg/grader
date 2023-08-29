class FechaHora:
    def __init__(self):
        self.fecha=''
        self.hora=''
        self.fechahora=''

    def __str__(self):
        return "{0}/{1}/{2} {3}".format(self.fechahora[6:10],self.fechahora[3:5],self.fechahora[0:2],self.fechahora[11:])
#(30-09-2015 17:45:00)
    def fijarFecha(self,fecha):
        lista=list(self.fechahora)
        lista[0:10]=fecha
        self.fechahora=''.join(lista)

    def fijarHora(self,hora):
        lista=list(self.fechahora)
        lista[11:]=hora
        self.fechahora=''.join(lista)

    def fijarFechaHora(self,fechahora):
        self.fecha=fechahora[0:10]
        self.hora=fechahora[11:]
        self.fechahora=fechahora

    def cambiar(self,parte):
        if parte[0:2]=='dd':
            lista=list(self.fechahora)
            lista[0]=parte[3]
            lista[1]=parte[4]
            self.fechahora=''.join(lista)
        elif parte[0:2]=='mm':
            lista=list(self.fechahora)
            lista[3]=parte[3]
            lista[4]=parte[4]
            self.fechahora=''.join(lista)
        elif parte[0:2]=='aa':
            lista=list(self.fechahora)
            #esto es necesario porque la petición podría ser aaaa = 2016, con un espacio entre medio
            #lo mismo podría suceder con los meses y los días
            parte=parte.split("=")
            parte=parte[1].replace(" ","")
            lista[6]=parte[0]
            lista[7]=parte[1]
            lista[8]=parte[2]
            lista[9]=parte[3]
            self.fechahora=''.join(lista)
        elif parte[0:2]=='HH':
            lista=list(self.fechahora)
            lista[11]=parte[3]
            lista[12]=parte[4]
            self.fechahora=''.join(lista)
        elif parte[0:2]=='MM':
            lista=list(self.fechahora)
            lista[14]=parte[3]
            lista[15]=parte[4]
            self.fechahora=''.join(lista)
        elif parte[0:2]=='SS':
            lista=list(self.fechahora)
            lista[17]=parte[3]
            lista[18]=parte[4]
            self.fechahora=''.join(lista)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

