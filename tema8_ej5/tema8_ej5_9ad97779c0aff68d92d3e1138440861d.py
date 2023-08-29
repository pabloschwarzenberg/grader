class FechaHora:
    def __init__(self,fecha,hora):
        self.fecha=fecha
        self.hora=hora

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
      string=""
      for i in range(0,len(self.fecha)):
          if self.fecha[i]!="/" and self.fecha[i]!="-":
            string=string+self.fecha[i]
            lista_fecha=list(string)
            i1_dia=lista_fecha[0]
            i2_dia=lista_fecha[1]
            i1_mes=lista_fecha[2]
            i2_mes=lista_fecha[3]
            i1_ano=lista_fecha[4]
            i2_ano=lista_fecha[5]
            i3_ano=lista_fecha[6]
            i4_ano=lista_fecha[7]
   
    def fijarHora(self,hora):
        stri=""
        for i in range(0,len(self.hora)):
          if self.hora[i]!=":":
            stri=stri+self.hora[i]
            lista_hora=list(stri)
            i1_hora=lista_hora[0]
            i2_hora=lista_hora[1]
            i1_min=lista_hora[2]
            i2_min=lista_hora[3]
            i1_seg=lista_hora[4]
            i2_seg=lista_hora[5]

    def fijarFechaHora(self,fechahora):
        self.fechahora=self.fecha+self.hora
        

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
           