class FechaHora:
    def __init__(self):
        self.fecha="dd-mm-aaaa"
        self.hora="HH:MM:SS"
        self.fechahora=self.fecha+" "+self.hora

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=" "+hora

    def fijarFechaHora(self,fechahora):
        self.fecha=fechahora[0:10]
        a=self.fecha[0:2]
        b=self.fecha[3:5]
        c=self.fecha[6:10]
        self.hora=fechahora[10:]
        self.fechahora=c+"/"+b+"/"+a+self.hora
        self.fecha=c+"/"+b+"/"+a

    def cambiar(self,parte):
        if "d" in parte:
            self.fecha=self.fecha.replace(self.fecha[0:2],parte[3:0])
            self.fechahora=self.fecha+self.hora
        if "m" in parte:
            self.fecha=self.fecha.replace(self.fecha[5:7],parte[3:])
            self.fechahora=self.fecha+self.hora
        if "a" in parte:
            self.fecha=self.fecha.replace(self.fecha[0:4],parte[7:])
            self.fechahora=self.fecha+self.hora
            
    def __str__(self):
        return self.fechahora
            

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    print("------------------")

    fh.cambiar("mm=10")
    print(fh)
    print("------------------")

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)