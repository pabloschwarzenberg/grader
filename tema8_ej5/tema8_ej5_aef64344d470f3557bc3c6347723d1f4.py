class FechaHora:
    def __init__(self):
        self.hola=""

    def __str__(self):
        return "{0}".format(self.hola)

    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
        hi=self.hola.split(" ")
        self.hola=hi[0]+" "+hora
        return self

    def fijarFechaHora(self,fechahora):
        hi=fechahora.split(" ")
        his=hi[0].split("-")
        hiss=his[2]+"/"+his[1]+"/"+his[0]
        self.hola=hiss+" "+hi[1]
        return self

    def cambiar(self,parte):
        his=[]
        hi=parte.split("=")
        for i in hi:
            d=i.strip()
            his.append(d)
        if his[0]=="mm":
            uno=self.hola[:5]
            dos=self.hola[7:]
            self.hola=uno+his[1]+dos
        elif his[0]=="aaaa":
            hiss=self.hola[4:]
            self.hola=his[1]+hiss
        return self

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           