class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        s=self.ano+'/'+self.mes+'/'+self.dia+' '+self.hora+':'+self.minutos+':'+self.segundos
        return s

    def fijarFecha(self,fecha):
        if '-' in fecha:
            fecha=fecha.split('-')
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]
        elif '/' in fecha:
            fecha=fecha.split('/')
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]

    def fijarHora(self,hora):
        hora=hora.split(':')
        self.hora=hora[0]
        self.minutos=hora[1]
        self.segundos=hora[2]

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(' ')
        fecha=fechahora[0]
        hora=fechahora[1]
        self.fijarHora(hora)
        self.fijarFecha(fecha)

    def cambiar(self,parte):
        parte=parte.split('=')
        c=[]
        for i in parte:
            i=i.rstrip()
            i=i.lstrip()
            c.append(i)
        if c[0]=='dd':
            self.dia=c[1]
        elif c[0]=='mm':
            self.mes=c[1]
        elif c[0]=='aaaa':
            self.ano=c[1]
        elif c[0]=='HH':
            self.hora=c[1]
        elif c[0]=='MM':
            self.minutos=c[1]
        elif c[0]=='SS':
            self.segundos=c[1]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           