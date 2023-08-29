class FechaHora:
    def __init__(self):
        self.fechahora=[0,0]
        fecha=self.fechahora[0]
        hora=self.fechahora[1]
    def __str__(self):
        if self.fechahora[0].find("/")!=-1:
            listaf=self.fechahora[0].split("/")
            if len(listaf[0])==2:
                d=listaf[0]
                a=listaf[2]
                listaf[0]=a
                listaf[2]=d
                strp="/".join(listaf)
        elif self.fechahora[0].find("-")!=-1:
            listaf=self.fechahora[0].split("-")
            if len(listaf[0])==2:
                d=listaf[0]
                a=listaf[2]
                listaf[0]=a
                listaf[2]=d
                strp="/".join(listaf)
        lista_imprimir=[strp," ",self.fechahora[1]]
        imprimir="".join(lista_imprimir)
        return imprimir

    def fijarFecha(self,fecha):
        self.fecha=fecha
        self.fechahora[0]=fecha
    def fijarHora(self,hora):
        self.hora=hora
        self.fechahora[1]=hora
    def fijarFechaHora(self,fechahora):
        listafh=fechahora.split(" ")
        self.fechahora=listafh

    def cambiar(self,parte):
        listap=parte.split("=")
        listah=self.fechahora[1].split(":")
        if self.fechahora[0].find("/")!=-1:
            listaf=self.fechahora[0].split("/")
        elif self.fechahora[0].find("-")!=-1:
            listaf=self.fechahora[0].split("-")
        if parte.find("dd")!=-1:
            listaf[0]=listap[1]
        if parte.find("mm")!=-1:
            listaf[1]=listap[1]
        if parte.find("aaaa")!=-1:
            listaf[2]=listap[1]
        if parte.find("HH")!=-1:
            listah[0]=listap[1]
        if parte.find("MM")!=-1:
            listah[1]=listap[1]
        if parte.find("SS")!=-1:
            listah[2]=listap[1]
        self.fechahora[0]="/".join(listaf) 
        self.fechahora[1]=":".join(listah)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           
