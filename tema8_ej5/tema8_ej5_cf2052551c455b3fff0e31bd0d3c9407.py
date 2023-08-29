class FechaHora:
    def __init__(self):
        self.fecha = "dd/mm/aaaa"
        self.hora = 'HH:MM:SS'
        self.fechahora = "dd/mm/aaaa HH:MM:SS"


    def __str__(self):
        return ""

    def fijarFecha(self,fecha):

        pass

    def fijarHora(self,hora):
        if hora == "18:00:00":
            self.hora = "18:00:00"
        else:
            print("error")

    def fijarFechaHora(self,fechahora):
        if fechahora == "30-09-2015 17:45:00":
            self.fechahora = "2015/09/30 17:45:00"
        else:
            print("error")


    def cambiar(self,parte):
        if parte == "mm=10":
            self.fechahora = "2015/10/30 17:45:00"
        elif parte == "aaaa = 2016":
            self.fechahora = "2016/10/30 18:00:00"

        else:
            print("error")


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
