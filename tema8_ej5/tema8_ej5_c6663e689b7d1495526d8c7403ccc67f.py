class FechaHora:
    def __init__(self):
        self.dia=0
        self.mes=0
        self.año=0
        self.hora=0
        self.minuto=0
        self.segundo=0

    def __str__(self):
        return(self.año+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.minuto+":"+self.segundo)

    def fijarFecha(self,fecha):
        if "/" in fecha:
            listafe=fecha.split("/")
            self.dia=listafe[0]
            self.mes=listafe[1]
            self.año=listafe[2]
        if "-" in fecha:
            listafe=fecha.split("-")
            self.dia=listafe[0]
            self.mes=listafe[1]
            self.año=listafe[2]

    def fijarHora(self,hora):
        listaho=hora.split(":")
        self.hora=listaho[0]
        self.minuto=listaho[1]
        self.segundo=listaho[2]
    
    def fijarFechaHora(self,fechahora):
        listafeho=fechahora.split(" ")
        self.fijarFecha(listafeho[0])
        self.fijarHora(listafeho[1])
        
    def cambiar(self,parte):
        parametro=parte.split("=")
        parametros=[]
        for i in parametro:
            x=i.strip(" ")
            parametros.append(x)
        if parametros[0]=="dd":
            if int(parametros[1])<31 and int(parametros[1])>0:
                self.dia=parametros[1]
            else:
                print("No es un valor válido para día")
        elif parametros[0]=="mm":
            if int(parametros[1])>0 and int(parametros[1])<13:
                self.mes=parametros[1]
            else:
                print("No es un valor válido para mes")
        elif parametros[0]=="aaaa":
            self.año=parametros[1]
        elif parametros[0]=="HH":
            if int(parametros[1])<24 and int(parametros[1])>=0:
                self.hora=parametros[1]
            else:
                print("No es un valor válido para hora. Tener en cuenta que medianoche es 00")
        elif parametros[0]=="MM":
            if int(parametros[1])<60 and int(parametros[1])>=0:
                self.minuto=parametros[1]
            else:
                print("No es un valor válido para minutos")
        elif parametros[0]=="SS":
            if int(parametros[1])<60 and int(parametros[1])>=0:
                self.segundo=parametros[1]
            else:
                print("No es un valor válido para segundos")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           