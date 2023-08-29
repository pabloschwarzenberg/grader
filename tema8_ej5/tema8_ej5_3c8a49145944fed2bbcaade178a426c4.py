class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        dato= fecha.split("-")
        dd= dato[0]
        mm= dato[1]
        aaaa= dato[2]
        return str(aaaa)+"/"+str(mm)+"/"+str(dd)

    def fijarHora(self,hora):
        info= hora.split(":")
        HH= info[0]
        MM= info[1]
        SS= info[2]
        return str(HH)+":"+str(MM)+":"+str(SS)


    def fijarFechaHora(self,fechahora):
        dato= fechahora.split(" ")
        a=(str(dato[0]))
        b=(str(dato[1]))
        c= self.fijarFecha(a)
        d= self.fijarHora(b)

        return str(c)+" "+str(d)

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
           