class FechaHora:
    def __init__(self):
        self.fecha="dd/mm/aaaa"
        self.hora="HH:MM:SS"

    def __str__(self):
        aux=""
        self.fecha=self.fecha.replace('/',',')
        self.fecha=self.fecha.replace('-',',')
        L=self.fecha.split(',')
        aux+=L[2]+"/"+L[1]+"/"+L[0]+" "+self.hora
        return aux

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        self.fecha=fechahora[0:10]
        self.hora=fechahora[11:]

    def cambiar(self,parametro):
        self.fecha=self.fecha.replace('/',',')
        self.fecha=self.fecha.replace('-',',')
        L=self.fecha.split(',')
        W=self.hora.split(':')
        if parametro[0]=="d":
          d=parametro[3:]
          d=int(d)
          if d<=31:
            L[0]=parametro[3:]
          else:
            print("aprendete las fechas")
        elif parametro[0]=="m":
          m=parametro[3:]
          m=int(m)
          if m<=12:
            L[1]=parametro[3:]
          else:
            print("en serio?")
        elif parametro[0]=="a":
          L[2]=parametro[7:]
        elif parametro[0]=="H":
          H=parametro[3:]
          H=int(H)
          if H<=24:
            W[0]=parametro[3:]
          else:
            return("wn pls, las horas llegan hasta el 24")
        elif parametro[0]=="M":
          M=parametro[3:]
          M=int(M)
          if M<=60:
            W[1]=parametro[3:]
          else:
            print("yashao")
        elif parametro[0]=="S":
          S=parametro[3:]
          S=int(S)
          if S<=60:
            W[2]=parametro[3:]
          else:
            ("SEGUÍ JUGANDO WN?, YA VIRATE, SI ERÍ MUY AWEONAO")
        q="/"
        x=":"
        self.fecha=q.join(L)
        self.hora=x.join(W)    

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)