import re
class FechaHora:
    def __init__(self):
        self.dia=0
        self.año=0
        self.mes=0
        self.hora=0
        self.minuto=0
        self.segundo=0

    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(self.año,self.mes,self.dia,self.hora,self.minuto,self.segundo)

    def fijarFecha(self,fecha):
        if fecha.find("/")!=-1:
            lista=fecha.split("/")
            self.dia=lista[0]
            self.mes=lista[1]
            self.año=lista[2]
        else:
            lista=fecha.split("-")
            self.dia=lista[0]
            self.mes=lista[1]
            self.año=lista[2]
        pass

    def fijarHora(self,hora):
        lista=hora.split(":")
        self.hora=lista[0]
        self.minuto=lista[1]
        self.segundo=lista[2]
        pass

    def fijarFechaHora(self,fechahora):
        lista=fechahora.split()
        
        self.dia=lista[0]
        self.mes=lista[1]
        self.año=lista[2]
        self.hora=lista[3]
        self.minuto=lista[4]
        self.segundo=lista[5]
        pass

    def cambiar(self,parte):
        if parte.find("dd")!=-1:
            lista=parte.split("=")
            if int(lista[1])>31:
                return("Este no es un valor valido")
            else:
                self.dia=lista[1]
        if parte.find("mm")!=-1:
            lista=parte.split("=")
            if int(lista[1])>12:
                return("Este no es un valor valido")
            else:
                self.mes=lista[1]
        if parte.find("aaaa")!=-1:
            lista=parte.split("=")
            self.año=lista[1]
        if parte.find("HH")!=-1:
            lista=parte.split("=")
            if int(lista[1])>24:
                return("Este no es un valor valido")
            else:
                self.hora=lista[1]
        if parte.find("MM")!=-1:
            lista=parte.split("=")
            if int(lista[1])>60:
                return("Este no es un valor valido")
            else:
                self.minuto=lista[1]
        if parte.find("SS")!=-1:
            lista=parte.split("=")
            if int(lista[1])>60:
                return("Este no es un valor valido")
            else:
                self.segundo=lista[1]
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
           