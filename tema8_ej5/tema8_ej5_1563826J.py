class FechaHora:
    def __init__(self):
        self.fecha='dd/mm/aaaa'
        self.hora='HH:MM:SS'
        return
    def __str__(self):
        list_fecha=self.fecha.split('/')
        dd=list_fecha[0]
        mm=list_fecha[1]
        aaaa=list_fecha[2]
        list_fecha=[aaaa,mm,dd]
        slash='/'
        self.fecha=slash.join(list_fecha)
        return '{0} {1}'.format(self.fecha,self.hora)
        
    def fijarFecha(self,fecha):
        self.fecha=fecha
        pass
    def fijarHora(self,hora):
        self.hora=hora
        pass
    def fijarFechaHora(self,fechahora):
        lista_fechahora=fechahora.split(' ')
        self.fecha=lista_fechahora[0]
        self.hora=lista_fechahora[1]
        pass
    def cambiar(self,parte):
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
           