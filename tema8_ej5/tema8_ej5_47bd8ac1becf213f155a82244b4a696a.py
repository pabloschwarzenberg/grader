class FechaHora:
    def __init__(self):
        self.dd=0
        self.mm=0
        self.aaaa=0
        self.HH=0
        self.MM=0
        self.SS=0

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.aaaa,self.mm,self.dd,self.HH,self.MM,self.SS)

    def fijarFecha(self,fecha):
        for i in fecha:
            if i=="/" or i=="-":
                fecha=fecha.split(i)
                break
        self.dd=fecha[0]
        self.mm=fecha[1]
        self.aaaa=fecha[2]
    def fijarHora(self,hora):
        hora=hora.split(":")
        self.HH=hora[0]
        self.MM=hora[1]
        self.SS=hora[2]
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fecha=fechahora[0]
        for i in fecha:
            if i=="/" or i=="-":
                fecha=fecha.split(i)
                break
        self.dd=fecha[0]
        self.mm=fecha[1]
        self.aaaa=fecha[2]
        hora=fechahora[1]
        hora=hora.split(":")
        self.HH=hora[0]
        self.MM=hora[1]
        self.SS=hora[2]
    def cambiar(self,parte):
        parte=parte.replace(" ","")
        parte=parte.split("=")
        if parte[0][0]=="d":
            dia=parte[1]
            if 31<int(dia) or int(dia)<1:
                return "Número fuera de rango."
            else:
                if len(dia)==1:
                    self.dd="0"+dia
                else:
                    self.dd=dia
        elif parte[0][0]=="m":
            mes=parte[1]
            if int(mes)>12 or int(mes)<1:
                return "Número fuera de rango."
            else:
                if len(mes)==1:
                    self.mm="0"+mes
                else:
                    self.mm=mes
        elif parte[0][0]=="a":
            self.aaaa=parte[1]
        elif parte[0][0]=="H":
            hora=parte[1]
            if 24<=int(hora):
                return "Número fuera de rango."
            else:
                if len(hora)==1:
                    self.HH="0"+hora
                else:
                    self.HH=hora
        elif parte[0][0]=="M":
            minuto=parte[1]
            if int(minuto)>=60:
                return "Número fuera de rango."
            else:
                if len(minuto)==1:
                    self.MM="0"+minuto
                else:
                    self.MM=minuto
        elif parte[0][0]=="S":
            sec=parte[1]
            if int(sec)>=60:
                return "Número fuera de rango."
            else:
                if len(sec)==1:
                    self.SS="0"+sec
                else:
                    self.SS=sec
                    

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
