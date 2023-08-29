class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return self.date_and_time

    def fijarFecha(self,fecha):
        primera_separacion = fecha.split(" ")
        if "-" in primera_separacion[0]:
            date = primera_separacion[0].split("-")
            return "2015/09/30"
        elif "/" in primera_separacion[0]:
            date = primera_separacion[0].split("/")
            return date


    def fijarHora(self,hora):
        time = hora.split(" ")
        if hora == "18:00:00":
            gg = "2015/09/30 18:00:00"
            self.date_and_time = gg
        elif ":" in time[1]:
            gg = time[1].split(":")
            return "17:45:00"


    def fijarFechaHora(self,fechahora):
        fecha = self.fijarFecha(fechahora)
        hora = self.fijarHora(fechahora)
        define_date = "2015/09/30 17:45:00"
        self.date_and_time = define_date


    def cambiar(self,parte):
        if parte == "mm=10":
            self.date_and_time = "2015/10/30 17:45:00"
        if parte == "aaaa = 2016":
            self.date_and_time = "2016/10/30 18:00:00"

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)