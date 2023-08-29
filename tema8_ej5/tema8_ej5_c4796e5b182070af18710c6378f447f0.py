class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
      def __init__(self,dd,mm,aaaa):
        self.dd=dd
        self.mm=mm
        self.aaaa=aaaa
       
        pass

    def fijarHora(self,hora):
      def __init__(self,HH,MM,SS):
        self.HH=HH
        self.MM=MM
        self.SS=SS
        
        pass

    def fijarFechaHora(self,fechahora):
      def __init__(self,fecha,hora):
        self.fecha=fecha
        self.hora=hora
        pass

    def cambiar(self,parte):  #FALTAN LOS ULTIMOS DOS PUNTOS#
    
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           