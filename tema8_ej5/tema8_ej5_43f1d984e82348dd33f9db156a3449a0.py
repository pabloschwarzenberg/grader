class FechaHora:
    def __init__(self):
        self.fecha=0
        self.hora=0

    def __str__(self):
        o=self.fecha
        O=o.split("-")
        p=[]
        for q in reversed(O):
            p.append(q)
        P="/".join(p)
        z="{0}{1}".format(P,self.hora)
        if " " in z:
            return z
        else:
            z="{0} {1}".format(P,self.hora)
            return z

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        self.fecha=fechahora[0:10]
        self.hora=fechahora[10:(len(fechahora)+1)]

    def cambiar(self,parte):
        if "dd" in parte:
            a=parte.split("=")
            a=int(a[1].strip())
            if a<32:
                b=self.fecha
                b=b.split("-")
                b[0]=str(a)
                self.fecha="-".join(b)
            else:
                return "ingrese un dato acorde al parámetro establecido"
        elif "mm" in parte:
            a=parte.split("=")
            a=int(a[1].strip())
            if a<13:
                b=self.fecha
                b=b.split("-")
                b[1]=str(a)
                self.fecha="-".join(b)
            else:
                return "ingrese un dato acorde al parámetro establecido"
        elif "aaaa" in parte:
            a=parte.split("=")
            a=a[1].strip()
            b=self.fecha
            b=b.split("-")
            b[2]=a
            self.fecha="-".join(b)
        elif "HH" in parte:
            a=parte.split("=")
            a=int(a[1].strip())
            if a<25:
                b=self.hora
                b=b.split(":")
                b[0]=str(a)
                self.hora=":".join(b)
            else:
                return "ingrese un dato acorde al parámetro establecido"
        elif "MM" in parte:
            a=parte.split("=")
            a=int(a[1].strip())
            if a<61:
                b=self.hora
                b=b.split(":")
                b[1]=str(a)
                self.hora=":".join(b)
            else:
                return "ingrese un dato acorde al parámetro establecido"
        elif "SS" in parte:
            a=parte.split("=")
            a=int(a[1].strip())
            if a<61:
                b=self.hora
                b=b.split(":")
                b[2]=str(a)
                self.hora=":".join(b)
            else:
                return "ingrese un dato acorde al parámetro establecido"

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
