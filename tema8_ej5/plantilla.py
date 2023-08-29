class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
        pass

    def fijarFechaHora(self,fechahora):
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









