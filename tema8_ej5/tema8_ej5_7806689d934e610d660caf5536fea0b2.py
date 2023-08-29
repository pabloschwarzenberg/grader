#aaaa/mm/dd HH:MM:SS
class FechaHora:
    def __init__(self):
        self.aaaa=""
        self.mm=""
        self.dd=""
        self.fecha=(self.aaaa+"-"+self.mm+"-"+self.dd)
        self.HH=""
        self.MM=""
        self.SS=""
        self.hora=(self.SS+":"+self.MM+":"+self.HH)

    def __str__(self):
        return ""+str(self.fecha)+" "+str(self.hora)

    def fijarFecha(self,fecha):
        fecha=fecha.split("-")
        self.aaaa=fecha[2]
        self.mm=fecha[1]
        self.dd=fecha[0]
        self.fecha=self.aaa+"/"+self.mm+"/"+self.dd
        return self.fecha

    def fijarHora(self,hora):
        hora=hora.split(":")
        self.HH=hora[2]
        self.MM=hora[1]
        self.SS=hora[0]
        self.hora=self.SS+":"+self.MM+":"+self.MM
        return self.hora

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        fechahora[0]=fechahora[0].split("-")#fecha
        fechahora[1]=fechahora[1].split(":")#hora
        self.aaaa=fechahora[0][2]
        self.mm=fechahora[0][1]
        self.dd=fechahora[0][0]
        self.fecha=self.aaaa+"/"+self.mm+"/"+self.dd
        self.HH=fechahora[1][2]
        self.MM=fechahora[1][1]
        self.SS=fechahora[1][0]
        self.hora=self.SS+":"+self.MM+":"+self.HH
        return self.fecha+" "+self.hora
        
#aaaa/mm/dd HH:MM:SS
    def cambiar(self,parte):
        for i in parte:
            if i.isalnum()==False:
                a=parte.find(i)
        parte=parte.split(parte[a])
        if parte[0]=="aaaa":
            self.aaaa=parte[-1]
        elif parte[0]=="mm":
            self.mm=parte[-1]
        elif parte[0]=="dd":
            self.dd=parte[-1]
        elif parte[0]=="HH":
            self.HH=parte[-1]
        elif parte[0]=="MM":
            self.MM=parte[-1]
        elif parte[0]=="SS":
            self.SS=parte[-1]
        self.fecha=self.aaaa+"/"+self.mm+"/"+self.dd
        self.hora=self.SS+":"+self.MM+":"+self.HH
        
        return self.fecha+" "+self.hora
                

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    fh.cambiar("mm=10")
    print(fh)
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)


   
           