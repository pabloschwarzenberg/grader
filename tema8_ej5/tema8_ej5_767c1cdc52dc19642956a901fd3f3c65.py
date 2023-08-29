class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
    def __str__(self):
        return self.fecha[6:] +"/"+ self.fecha[3:5] + "/" + self.fecha[0:2]+ " "+self.hora
    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        self.hora=fechahora[1]
        self.fecha=fechahora[0]
    def cambiar(self,parte):
        parte = parte.replace(" ","")
        parte=parte.split("=")
        if parte[0]=="dd":
            if len(parte[1])==2:
                self.fecha=self.fecha.replace(self.fecha[0:2],parte[1])
            if len(parte[1])==1:
                self.fecha=self.fecha.replace(self.fecha[0:2],"0"+parte[1])
        if parte[0]=="mm":
            if len(parte[1])==2:
                self.fecha=self.fecha.replace(self.fecha[3:5],parte[1])
            if len(parte[1])==1:
                self.fecha=self.fecha.replace(self.fecha[3:5],"0"+parte[1])
        if parte[0]=="aaaa":
            self.fecha=self.fecha.replace(self.fecha[6:],parte[1])
        if parte[0]=="HH":
            if len(parte[1])==2:
                self.hora=self.hora.replace(self.hora[0:2],parte[1])
            if len(parte[1])==1:
                self.hora=self.hora.replace(self.hora[0:2],"0"+parte[1])
        if parte[0] == "MM":
            if len(parte[1]) == 2:
                self.hora = self.hora.replace(self.hora[3:5], parte[1])
            if len(parte[1]) == 1:
                self.hora = self.hora.replace(self.hora[3:5], "0" + parte[1])
        if parte[0] == "SS":
            if len(parte[1]) == 2:
                self.hora = self.hora.replace(self.hora[6:], parte[1])
            if len(parte[1]) == 1:
                self.hora = self.hora.replace(self.hora[6:], "0" + parte[1])


fh=FechaHora()
fh.fijarFechaHora("30-09-2015 17:45:00")
print(fh)

fh.cambiar("mm=10")
print(fh)

fh.fijarHora("18:00:00")
fh.cambiar("aaaa = 2016")
print(fh)




if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           