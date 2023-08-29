class FechaHora:
    def __init__(self):
        self.dd=0
        self.mm=0
        self.aaaa=0
        self.HH=0
        self.MM=0
        self.SS=0

    def __str__(self):
        return "'{0}/{1}/{3} {4}:{5}:{6}".format(self.aaaa,self.mm,self.dd,self.HH,self.MM,self.SS)

    def fijarFecha(self,fecha):
        if fecha.find('/')!=-1:
          f=fecha.split('/')
          self.dd=f[0]
          self.mm=f[1]
          self.aaaa=f[2]
        elif fecha.find('-')!=-1:
          f=fecha.split('_')
          self.dd=f[0]
          self.mm=f[1]
          self.aaaa=f[2]
    def fijarHora(self,hora):
          h=hora.split(':')
          self.HH=h[0]
          self.MM=h[1]
          self.SS=h[2]

    def fijarFechaHora(self,fechahora):
        fh=fechahora.split(' ')
        f=fh[0].split('/')
        self.dd=f[0]
        self.mm=f[1]
        self.aaaa=f[2]
        h=fh[1].split(':')
        self.HH=h[0]
        self.MM=h[1]
        self.SS=h[2]

    def cambiar(self,parte):
        p=parte.split('=')
        if p[0]==dd:
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
           