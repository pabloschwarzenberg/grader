class FechaHora:
    def __init__(self):
        self.dia="dd"
        self.mes="mm"
        self.ano="aaaa"
        self.horas="HH"
        self.minutos="MM"
        self.segundos="SS"
       

    def __str__(self):
        return self.ano+"/"+self.mes+"/"+self.dia+" "+self.horas+":"+self.minutos+":"+self.segundos

    def fijarFecha(self,fecha="dd-mm-aaaa"):
        self.dia=fecha[0:2]
        self.mes=fecha[3:5]
        self.ano=fecha[6:10]
        
        

    def fijarHora(self,hora="HH:MM:SS"):
        self.horas=hora[0:2]
        self.minutos=hora[3:5]
        self.segundos=hora[6:8]

    def fijarFechaHora(self,fechahora="dd-mm-aaaa HH:MM:SS"):
        self.dia=fechahora[0:2]
        self.mes=fechahora[3:5]
        self.ano=fechahora[6:10]
        self.horas=fechahora[11:13]
        self.minutos=fechahora[14:16]
        self.segundos=fechahora[17:19]
        fechahora=self.dia+"-"+self.mes+"-"+self.ano+" "+self.horas+":"+self.minutos+":"+self.segundos

    def cambiar(self,parte):
        if parte[0:2]=="dd" and int(parte[3:])<=31:
            self.dia=parte[3:]
        elif parte[0:2]=="mm" and int(parte[3:])<=12:
            self.mes=parte[3:]
        elif parte[0:2]=="aa" and int(parte[7:])<=2016:
            self.ano=parte[7:]
        elif parte[0:2]=="HH" and int(parte[3:])<=24:
            self.horas=parte[3:]
        elif parte[0:2]=="MM" and int(parte[3:])<=59:
            self.minutos=parte[3:]
        elif parte[0:2]=="SS" and int(parte[3:])<=59:
            self.segundos=parte[3:]
        
            
        
    

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)




           