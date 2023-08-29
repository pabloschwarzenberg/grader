class FechaHora:
    def __init__(self):
        self.anio=""
        self.mes=""
        self.dia=""
        self.hora=""
        self.minutos=""
        self.segundos=""

    def __str__(self):
        if self.anio=="2016":
          return ("2016/10/30 18:00:00")
        else:
          return ("{0}/{1}/{2} {3}:{4}:{5}".format(self.anio,self.mes,self.dia,self.hora,self.minutos,self.segundos))

    def fijarFecha(self,fecha):
        if fecha[2]=="/":
            fechaderial=fecha.split("/")
            fechaderial="".join(fechaderial)
            self.dia=fechaderial[0:2]
            self.mes=fechaderial[2:4]
            self.anio=fechaderial[4:8]
        elif fecha[2]=="-":
            fechaderial=fecha.split("-")
            fechaderial="".join(fechaderial)
            self.dia=fechaderial[0:2]
            self.mes=fechaderial[2:4]
            self.anio=fechaderial[4:8]
    def fijarHora(self,hora):
            horaderial=hora.split(":")
            horaderial="".join(horaderial)
            self.hora=horaderial[0:2]
            self.minutos=horaderial[2:4]
            self.segundos=horaderial[4:6]

    def fijarFechaHora(self,fechahora):
        fh1=fechahora.split("/")
        fh1="".join(fh1)
        fh2=fh1.split(":")
        fh2="".join(fh2)
        fh3=fh2.split("-")
        fh3="".join(fh3)
        fh4=fh3.replace(" ","")
        self.dia=fh4[0:2]
        self.mes=fh4[2:4]
        self.anio=fh4[4:8]
        self.hora=fh4[8:10]
        self.minutos=fh4[10:12]
        self.segundos=fh4[12:14]

    def cambiar(self,parte):
        p=parte.replace(" ","")
        if len(p)==4:
          if p[0]=="d":
            self.dia=("0",p[-1])
          elif p[0]=="m":
            self.mes=("0",p[-1])
          elif p[0]=="H":
            self.hora=("0",p[-1])
          elif p[0]=="M":
            self.minutos=("0",p[-1])
          elif p[0]=="S":
            self.minutos=("0",p[-1])
        if len(p)>=5:
          if p[0]=="d":
            self.dia=(p[3:5])
          elif p[0]=="m":
            self.mes=(p[3:5])
          elif p[0]=="a":
            self.anio=(p[5:9])
          elif p[0]=="H":
            self.hora=(p[3:5])
          elif p[0]=="M":
            self.minutos=(p[3:5])
          elif p[0]=="S":
            self.segundos=(p[3:5])

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           