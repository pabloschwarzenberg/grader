class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        self.fecha=fecha
        fecha= int(input("ingrese fecha: (dd/mm/aa) "))
        pass

    def fijarHora(self,hora):
        self.hora=hora
        hora= int(input("ingrese hora: (HH/MM/SS) "))
        pass

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora
        hora= int(input("ingrese fechahora: (HH/MM/SS)(dd/mm/aa) "))
        pass

    def cambiar(self,parte):
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
           