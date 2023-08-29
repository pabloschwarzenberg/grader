class FechaHora:
    def __init__(self):
        self.d = ""
        self.m = ""
        self.a = ""
        self.h = ""
        self.min = ""
        self.s = ""
        pass

    def __str__(self):
        s = str(self.a) + "/" + str(self.m) + "/" + str(self.d) + " " + str(self.h) + ":" + str(self.min) + ":" + str(
            self.s)
        return s

    def fijarFecha(self, fecha):
        if "/" in fecha:
            imp = fecha.split("/")
            self.d = int(imp[0].strip())
            self.m = int(imp[1].strip())
            self.a = int(imp[2].strip())
        elif "-" in fecha:
            imp = fecha.split("-")
            self.d = int(imp[0].strip())
            self.m = int(imp[1].strip())
            self.a = int(imp[2].strip())
        return
        pass

    def fijarHora(self, hora):
        imp = hora.split(":")
        self.h = int(imp[0].strip())
        self.min = int(imp[1].strip())
        self.s = int(imp[2].strip())
        return

    def fijarFechaHora(self, fechahora):
        imp = fechahora.split(" ")
        self.fijarFecha(imp[0])
        self.fijarHora(imp[1])
        return

    def cambiar(self, parte):
        imt = parte.split("=")
        if imt[0].strip() == "dd":
            self.d = int(imt[1])
        elif imt[0].strip() == "mm":
            self.m = int(imt[1])
        elif imt[0].strip() == "aaaa":
            self.a = int(imt[1])
        elif imt[0].strip() == "HH":
            self.h = int(imt[1])
        elif imt[0].strip() == "MM":
            self.min = int(imt[1])
        elif imt[0].strip() == "SS":
            self.s = int(imt[1])
        return


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)