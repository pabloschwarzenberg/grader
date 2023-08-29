class FechaHora:
    def __init__(self):
        self.dia=00
        self.mes=00
        self.año=0000
        self.hora=00
        self.min=00
        self.seg=00

    def __str__(self):
        return '{0}/{1}/{2} {3}:{4}:{5}'.format(self.año,self.mes,self.dia,self.hora,self.min,self.seg)

    def fijarFecha(self, fecha):
        self.dia=fecha[0:2]
        self.mes=fecha[3:5]
        self.año=fecha[6:10]

    def fijarHora(self, hora):
        self.hora = hora[0:2]
        self.min = hora[3:5]
        self.seg = hora[6:8]

    def fijarFechaHora(self, fechahora):
        self.dia = fechahora[0:2]
        self.mes = fechahora[3:5]
        self.año = fechahora[6:10]
        self.hora = fechahora[11:13]
        self.min = fechahora[14:16]
        self.seg = fechahora[17:19]

    def cambiar(self, parte):
        if parte[0:2]=='dd':
            self.dia=parte[3:]
        elif parte[0:2] == 'mm':
            self.mes = parte[3:]
        elif parte[0:2] == 'aa':
            self.año = parte[7:]
        elif parte[0:2] == 'HH':
            self.hora = parte[3:]
        elif parte[0:2] == 'MM':
            self.min = parte[3:]
        elif parte[0:2] == 'SS':
            self.seg = parte[3:]
            
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           