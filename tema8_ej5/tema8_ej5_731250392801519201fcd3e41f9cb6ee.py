class FechaHora:
    def __init__(self,fecha,hora):
        self.fecha= dd/mm/aa
        self.hora= HH:MM:SS

    def __str__(self):
        
        return ""

    def fijarFecha(self,dd/mm/aaaa):
        Fecha=self.dd/mm/aa

    def fijarHora(self,HH:MM:SS):
        cambiar
        Hora=self.HH:MM:SS

    def fijarFechaHora(self,dd/mm/aaaa HH:MM:SS):
        FechaHora= FechaHora(Fecha Hora)

    def cambiar(self,parametro,valor):
        if parametro==dd:
            if valor>=1 and valor <=31:
               self.dd/mm/aaaa=valor/mm/aaaa
        if parametro==mm:
            if valor>=1 and valor<=12:
               self.dd/mm/aaaa=dd/valor/aaaa
        if parametro==aaaa:
            if valor>=0 and valor <=100000000:
               self.dd/mm/aaaa=dd/mm/valor
        if parametro==HH:
            if valor>=0 and valor<=23:
                self.HH:MM:SS=valor:MM:SS
        if parametro==MM:
            if valor>=0 and valor<=59
               self.HH:MM:SS=HH:valor:SS
        if parametro=SS:
            if valor>=0 and valor<=59:
            self.HH:MM:SS=HH:MM:valor
            

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           