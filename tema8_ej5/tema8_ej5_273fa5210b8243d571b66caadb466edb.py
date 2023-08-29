class FechaHora:
    def __init__(self):
        self.dia = ''
        self.mes = ''
        self.ano = ''
        self.hora = ''
        self.minu = ''
        self.sec = ''
        

    def __str__(self):
        s = '{0}/{1}/{2} {3}:{4}:{5}'.format(self.ano, self.mes, self.dia, self.hora, self.minu, self.sec)        
        return s

    def fijarFecha(self,fecha):
        if fecha.find('/') != -1:
          fecha = fecha.split('/')
        elif fecha.find('-') != -1:
          fecha = fecha.split('-')
        if int(fecha[0]) in range(1,32) and int(fecha[1]) in range(1,13) and int(fecha[2]) > 0:
              self.dia = fecha[0]
              self.mes = fecha[1]
              self.ano = fecha[2]
        else:
            print('Fecha invalida')

    def fijarHora(self,hora):
        hora = hora.split(':')
        if int(hora[0]) in range(0,24) and int(hora[1]) in range(0,60) and int(hora[2]) in range(0,60):
          self.hora = hora[0]
          self.minu = hora[1]
          self.sec = hora[2]
        else:
            print('Hora invalida')

    def fijarFechaHora(self,fechahora):
      fechahora = fechahora.split(' ')
      fechax = fechahora[0]
      
      horax = fechahora[1]
      self.fijarFecha(fechax)
      self.fijarHora(horax)
      
    def cambiar(self,parte):
        p = ''
        for y in parte:
          if y != ' ':
            p += y
        parte = p
        parte = parte.split('=')
        if parte[0] == 'dd' and int(parte[1]) in range(1,32):
            self.dia = parte[1]
        elif parte[0] == 'mm' and int(parte[1]) in range(1,13):
            self.mes = parte[1]
        elif parte[0] == 'aaaa':
            self.ano = parte[1]
        elif parte[0] == 'HH' and int(parte[1]) in range(0,24):
            self.hora = parte[1]
        elif parte[0] == 'MM' and int(parte[1]) in range(0,60):
            self.minu = parte[1]
        elif parte[0] == 'SS' and int(parte[1]) in range(0,60):
            self.sec = parte[1]
        else:
          print('Valor invalido')

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           