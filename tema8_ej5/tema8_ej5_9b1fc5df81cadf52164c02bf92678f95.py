class FechaHora:
    def __init__(self):
        self.fecha = ''
        self.hora = ''

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.fecha[6:],self.fecha[3:5],self.fecha[0:2],self.hora[0:2],self.hora[3:5],self.hora[6:])

    def fijarFecha(self,fecha):
        self.fecha = fecha

    def fijarHora(self,hora):
        self.hora = hora

    def fijarFechaHora(self,fechahora):
        self.fecha = fechahora[0:10]
        self.hora = fechahora[10:18]

    def cambiar(self,parte):
        dia = parte.find('dd')
        mes = parte.find('mm')
        a = parte.find('aa')
        hora = parte.find('HH')
        minutos = parte.find('MM')
        segundos = parte.find('SS')
        if dia!=-1:
          d = parte.split('=')
          if int(d[1])<=31 and int(d[1])>=1:
            self.fecha[0:2] = d[1]
          else:
            print('Error')
        elif mes!=-1:
          m = parte.split('=')
          if int(m[1])>=1 and int(m[1])<=12:
            self.fecha[3:5] = m[1]
          else:
            print('Error')
        elif a!=-1:
          A = parte.split('=')
          self.fecha[6:10] = A[1]
        elif hora!=-1:
          h = parte.split('=')
          self.hora[0:2] = h[1]
        elif minutos!=-1:
          M = parte.split('=')
          self.hora[3:5] = M[1]
        elif segundos!=-1:
          s = parte.split('=')
          self.hora[6:] = s[1]


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           