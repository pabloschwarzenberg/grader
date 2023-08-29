class FechaHora:
    def __init__(self):
        self.hora=""
        self.minutos=""
        self.segundos=""
        self.dia=""
        self.mes=""
        self.ano=""
    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(self.ano,self.mes,self.dia,self.hora,self.minutos,self.segundos)

    def fijarFecha(self,fecha):
        fecha=list(fecha)
        for i in fecha:
          if i==("-") or i==("/"):
            fecha.remove(i)
        fecha_dia=fecha[0]+fecha[1]
        fecha_mes=fecha[2]+fecha[3]
        fecha_ano=fecha[4]+fecha[5]+fecha[6]
        self.dia=str(fecha_dia)
        self.mes=str(fecha_mes)
        self.ano=str(fecha_ano)

    def fijarHora(self,hora):
        hora=list(hora)
        for i in hora:
          if i==(":"):
            hora.remove(i)
        hora_hora=hora[0]+hora[1]
        hora_min=hora[2]+hora[3]
        hora_seg=hora[4]+hora[5]
        self.hora=str(hora_hora)
        self.minutos=str(hora_min)
        self.segundos=str(hora_seg)
    def fijarFechaHora(self,fechahora):
        fechahora=list(fechahora)
        for i in fechahora:
          if i ==("/") or i==(":"):
            fechahora.remove(i)
        fecha_dia2=fechahora[0]+fechahora[1]
        fecha_mes2=fechahora[2]+fechahora[3]
        fecha_ano2=fechahora[4]+fechahora[5]+fechahora[6]
        hora_hora2=fechahora[8]+fechahora[9]
        hora_min2=fechahora[10]+fechahora[11]
        hora_seg2=fechahora[12]+fechahora[13]
        self.dia=str(fecha_dia2)
        self.mes=str(fecha_mes2)
        self.ano=str(fecha_ano2)
        self.hora=str(hora_hora2)
        self.minutos=str(hora_min2)
        self.segundos=str(hora_seg2)

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
           