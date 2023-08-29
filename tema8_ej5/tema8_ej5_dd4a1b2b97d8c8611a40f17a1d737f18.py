class FechaHora:
    def __init__(self):
        self.fecha=[]
        self.hora=[]

    def __str__(self):
        if len(self.fecha[0])==2:
            self.fecha.reverse()
        s="/".join(self.fecha)
        m=":".join(self.hora)
        return s+" "+m

    def fijarFecha(self,fecha):
        if "-" in fecha:
            f=fecha.split("-")
            if self.fecha!=[]:
                self.fecha=[]  
            for i in f:
                self.fecha.append(i)
                self.fecha.reverse()
        elif "/" in fecha:
            f=fecha.split("/")
            if self.fecha!=[]:
                self.fecha=[] 
            for i in f:
                self.fecha.append(f[i])
                self.fecha.reverse()

    def fijarHora(self,hora):
        h=hora.split(":")
        if self.hora!=[]:
           self.hora=[]             
        for i in h:
            self.hora.append(i)


    def fijarFechaHora(self,fechahora):
        fh=fechahora.split(" ")
        f1=fh[0]
        if "-" in f1:
            f=f1.split("-")
            for i in f:
                self.fecha.append(i)
        elif "/" in f1:
            f=f1.split("/")
            for i in f:
                self.fecha.append(f[i])
        h1=fh[1]
        h=h1.split(":")
        for i in h:
            self.hora.append(i)

    def cambiar(self,parte):
        y=[]
        parte=parte.split("=")
        for i in parte:
            i=i.strip()
            y.append(i)
        if y[0]=="aaaa":
            if len(self.fecha[0])==2:
                self.fecha[2]=self.fecha[2].replace(self.fecha[2],y[1])
            if len(self.fecha[0])==4:
                self.fecha[0]=self.fecha[0].replace(self.fecha[0],y[1])
            return self.fecha
        if y[0]=="dd":
            if len(self.fecha[0])==2:
                self.fecha[0]=self.fecha[0].replace(self.fecha[0],y[1])
            if len(self.fecha[0])==4:
                self.fecha[2]=self.fecha[2].replace(self.fecha[2],y[1])
            return self.fecha
        if y[0]=="mm":
            self.fecha[1]=self.fecha[1].replace(self.fecha[1],y[1])
            return self.fecha
        if y[0]=="HH":
            self.hora[0]=self.hora[0].replace(self.hora[0],y[1])
            return self.hora
        if y[0]=="MM":
            self.hora[1]=self.hora[1].replace(self.hora[1],y[1])
            return self.hora
        if y[0]=="SS":
            self.hora[2]=self.hora[2].replace(self.hora[2],y[1])
            return self.hora

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           