class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        t = self.fecha.split("/")
        p = len(t[0])
        if p < 3:
            f = self.fecha.split("/")
            f = f[::-1]
            self.fecha = ("/").join(f)
            return self.fecha + " " + self.hora
        else:
            return self.fecha + " " + self.hora

    def fijarFecha(self, fecha):
        if fecha.find("-") != -1:
            s = fecha.split("-")
            self.fecha = ("/").join(s)
        else:
            self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fhg = fechahora.split(" ")
        self.fecha = fhg[0]
        self.hora = fhg[1]
        if self.fecha.find("-") != -1:
            d = self.fecha.split("-")
            self.fecha = "/".join(d)

    def cambiar(self, parte):
        if self.fecha.find("/") != -1:
            p = self.fecha.split("/")
            t = len(p[0])
            fechan = self.fecha.split("/")
            if t < 3:
                a = parte.split("=")
                a[0] = a[0].strip()
                a[1] = a[1].strip()
                if a[0] == "dd":
                    fechan[0] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "mm":
                    fechan[1] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "aaaa":
                    fechan[2] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
            else:
                fechan = fechan[::-1]
                a = parte.split("=")
                a[0] = a[0].strip()
                a[1] = a[1].strip()
                if a[0] == "dd":
                    fechan[0] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "mm":
                    fechan[1] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "aaaa":
                    fechan[2] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k

        elif self.fecha.find("-") != -1:
            p = self.fecha.split("-")
            t = len(p[0])
            fechan = self.fecha.split("-")
            if t < 3:
                a = parte.split("=")
                a[0] = a[0].strip()
                a[1] = a[1].strip()
                if a[0] == "dd":
                    fechan[0] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "mm":
                    fechan[1] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "aaaa":
                    fechan[2] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
            else:
                fechan = fechan[::-1]
                a = parte.split("=")
                a[0] = a[0].strip()
                a[1] = a[1].strip()
                if a[0] == "dd":
                    fechan[0] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "mm":
                    fechan[1] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
                elif a[0] == "aaaa":
                    fechan[2] = a[1]
                    k = "/".join(fechan)
                    self.fecha = k
        elif self.hora.find(":") != -1:
            horan = self.hora.split(":")
            if a[0] == "HH":
                horan[0] = a[1]
                g = ":".join(horan)
                self.hora = g
            elif a[0] == "MM":
                horan[1] = a[1]
                g = ":".join(horan)
                self.hora = g
            elif a[0] == "SS":
                horan[2] = a[1]
                g = ":".join(horan)
                self.hora = g


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    
    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)