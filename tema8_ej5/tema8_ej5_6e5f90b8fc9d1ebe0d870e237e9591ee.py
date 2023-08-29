class FechaHora:
    def __init__(self,fecha,hora):
        self.fecha=str(fecha)
        self.hora=str(hora)
        self.fechahora= str(self.fecha)+"  "+str(self.hora)


    def fijarHora(self,hora):
           self.hora=hora
    def fijarFecha(self,fecha):
        self.fecha= str(fecha)
        self.hora=self.hora
    def fijarFechaHora(self,fechahora):
        fecha= fechahora[0:10]
        self.fecha=fecha
        hora= fechahora[10:]
        self.hora=hora
    def cambiar(self,cambio):
        c=cambio.strip()
        if c[0]=="a":
            a= c[-4:]
            self.fecha= self.fecha[:-3]+a
        if c[0]=="m":
            a=c[-1:]
            if  0 < int(a) >13:
                     self.fecha=self.fecha[:3]+a+self.fecha[-4:]
            else:
                print("ingrese un mes enre 1 y 12 ")
        if c[0]=="d":
            a=c[-1:]
            if 0 < int(a) > 31:
                self.fecha= a+self.fecha[2:]
            else:
                print("ingrese un dia entre 1 y 31")

        if c[0]=="H":
            a = c[-1:]
            if -1 < int(a) and int(a) > 24:
                 self.hora= a+self.hora[2:]
            else:
                print("ingrese una hora entre 00 y 23")

        if c[0]=="M":
            a = c[-1:]
            if 0 < int(a) > 60:
                    self.hora= self.hora[:2]+a+self.hora[5:]
            else:
                print("ingrese un minuto entre 0 y 59")
        if  c[0] == "S":
            a = c[-1:]
            if 0 < int(a) > 60:
                 self.hora =  self.hora[:-1] +a
            else:
                print("ingrese un segundo entre 0 y 60 ")

    def __str__(self):
        s= self.fecha[-4:]+"/"+self.fecha[3:5]+"/"+self.fecha[:2]+" "+str(self.hora)
        self.fechahora = s
        y= str(self.fechahora)

        return y


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           