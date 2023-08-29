class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""

    def __str__(self):
        
        return ""

    def fijarFecha(self,fecha):
     
        return fecha
    
    def fijarHora(self,hora):
        a=1
        if a==1:
            self.hora=hora
            print(self.fecha+" "+self.hora)

    def fijarFechaHora(self,fechahora):
        self.dd=fechahora[0:2]
        self.mm=fechahora[3:5]
        self.aaaa=fechahora[6:10]
        self.HH=fechahora[11:13]
        self.MM=fechahora[14:16]
        self.SS=fechahora[17:19]
        self.hora=(self.HH+":"+self.MM+":"+self.SS)
        self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
        print(self.fecha+" "+self.hora)


    def cambiar(self,parte):
    
        if parte[0:2]=="dd":
            self.dd=parte[3:5]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            print(self.fecha+" "+self.hora)
            
        if parte[0:2]=="mm":
            self.mm=parte[3:5]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            print(self.fecha+" "+self.hora)
            
        if parte[0:2]=="aa":
            self.aaaa=parte[5:9]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            #print(self.fecha+" "+self.hora)
            
        if parte[0:2]=="HH":
            self.HH=parte[3:5]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            print(self.fecha+" "+self.hora)
            
        if parte[0:2]=="MM":
            self.MM=parte[3:5]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            print(self.fecha+" "+self.hora)
            
        if parte[0:2]=="SS":
            self.SS=parte[3:5]
            self.hora=(self.HH+":"+self.MM+":"+self.SS)
            self.fecha=(self.aaaa+"/"+self.mm+"/"+self.dd)
            print(self.fecha+" "+self.hora)
    
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
   #print(fh)

    fh.cambiar("mm=10")
   # print(fh)

    
    fh.cambiar("aaaa=2016")
    fh.fijarHora("18:00:00")
   # print(fh)
           
           