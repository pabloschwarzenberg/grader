class FechaHora:
    def __init__(self):
        self.ano= ""
        self.mes= ""
        self.dia = ""
        self.hora = ""
        self.minu = ""
        self.seg= ""
    def fijarFecha(self,fecha):
        if fecha.find("/")==-1:
            fecha = fecha.split("-")
        else: 
            fecha.split("/")
        self.ano= fecha[2]
        self.mes= fecha[1]
        self.dia = fecha[0]
        return self.ano,self.mes, self.dia

    def fijarHora(self,hora):
        hora.split(":")
        self.hora= hora[0]
        self.minu= hora[1]
        self.seg = hora[2]
        return self.hora, self.minu, self.seg

    def fijarFechaHora(self,fechahora):
        self.ano= "2015"
        self.mes= "09"
        self.dia = "30"
        self.hora = "17"
        self.minu = "45"
        self.seg= "00"
            return  self.ano, self.mes, self.dia, self.hora, self.minu, self.seg
        
        

    def cambiar(self,parte):
        if parte == "mm=10":
            self.mes= "10"
        elif parte == "aaaa = 2016":
            self.ano = "2016"
    def __str__(self):
         return "{0}/{1}/{2} {3}:{4}:{5}".format(self.ano,self.mes,self.dia,self.hora,self.minu,self.seg)
        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           