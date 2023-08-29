class FechaHora:
    def __init__(self):
        self.hora=""
        self.minutos=""
        self.segundos=""
        self.dia=""
        self.mes=""
        self.año=""

    def __str__(self):
        fh=self.año+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minutos+":"+self.segundos
        return fh

    def fijarFecha(self,fecha):
        dias=fecha.split("-")
        self.dia=dias[0]
        self.mes=dias[1]
        self.año=dias[2]
        return self
        

    def fijarHora(self,hora):
        time=hora.split(":")
        self.hora=time[0]
        self.minutos=time[1]
        self.segundos=time[2]
        return self
        
    def fijarFechaHora(self,fechahora):
        fe=fechahora[0:10]
        fe=fe.split("-")
        self.dia=fe[0]
        self.mes=fe[1]
        self.año=fe[2]
        ho=fechahora[11:]
        ho=ho.split(":")
        self.hora=ho[0]
        self.minutos=ho[1]
        self.segundos=ho[2]
        return self
    

    def cambiar(self,parte):
        if "dd" in parte:
            self.dia=parte[3:]
        if "mm" in parte:
            self.mes=parte[3:]
        if "aaaa" in parte:
            self.año=parte[7:]
        if "HH" in parte:
            self.hora=parte[3:]
        if "MM" in parte:
            self.minutos=parte[3:]
        if "SS" in parte:
            self.segundos=parte[3:]
        print(self.mes)
        
        return self
        
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    fh.cambiar("mm=10")
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)    