class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        self.fecha=fecha
            

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        a=fechahora.split(" ")
        self.fecha=a[0]
        self.hora=a[1]

    def cambiar(self,parte):
        b=parte.split("=")
        print(b)
        if b[0]=="dd":
            if self.fecha.count("/")>0:
                c=self.fecha.split("/")
                
                c[0]=b[1]
                "".join(c,2)
            if self.fecha.count("-")>0:
                
                c=self.fecha.split("/")
                
                c[0]=b[1]
                "".join(c,2)
                
        if b[0]=="mm":
            if self.fecha.count("/")>0:
                c=self.fecha.split("/")
                c[1]=b[1]
                "".join(c)
                print(c)
            if self.fecha.count("-")>0:
                c=self.fecha.split("-")
               
                c[1]=b[1]
                "".join(c)
        if b[0]=="aaaa":
            if self.fecha.count("/")>0:
                c=self.fecha.split("/")
                c[2]=b[1]
                "".join(c)
            if self.fecha.count("-")>0:
                c=self.fecha.split("-")
                c[2]=b[1]
                "".join(c)
        if b[0]=="HH":
            c=self.hora.split(":")
            c[0]=b[1]
        if b[0]=="MM":
            c=self.hora.split(":")
            c[1]=b[1]
        if b[0]=="SS":
            c=self.hora.split(":")
            c[2]=b[1]
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)


           