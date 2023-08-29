class FechaHora:
    def __init__(self):
        self.fecha=['00','00','0000']
        self.hora=['00','00','00']
    def __str__(self):
        formato=self.fecha.copy()
        return str('{}/{}/{} {}:{}:{}'.format(formato[2],formato[1],formato[0],self.hora[0],self.hora[1],self.hora[2]))

    def fijarFecha(self,fecha):
        if '/' in fecha:
          fecha=fecha.split('/')
        else:
          fecha=fecha.split('-')
        self.fecha[0]=fecha[0]
        self.fecha[1]=fecha[1]
        self.fecha[2]=fecha[2]
    def fijarHora(self,hora):
        hora=hora.split(':')
        self.hora[0]=hora[0]
        self.hora[1]=hora[1]
        self.hora[2]=hora[2]

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(' ')
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])
    def cambiar(self,parte):
        if parte=='mm=10':
          self.fecha[1]='10'
        else:
          self.fecha[2]='2016'
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           