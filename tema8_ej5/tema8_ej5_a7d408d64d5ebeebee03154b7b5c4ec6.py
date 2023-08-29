def ordenar(fecha):
    fecha=fecha.replace("-","/")
    b=fecha.split("/")
    if len(b[0])!=4:
        for e in b:
            if len(e)==4:
                aaaa=e
    fecha_f=aaaa + "/" + str(fecha)[3:6] + str(fecha)[0:2]
    return fecha_f
    
class FechaHora:
    def __init__(self):
        self.fecha=0
        self.hora=0

    def __str__(self):
        return (self.fecha.replace("-","/") + " " + self.hora)
        
    def __repr__(self):
        return self.__str__()

    def fijarFecha(self,fecha):
        self.fecha=ordenar(fecha)

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        a=fechahora.split(" ")
        self.fecha=ordenar(a[0])
        self.hora=a[1]

    def cambiar(self,parte):
        a=parte.replace(" ","").split("=")
        if a[0]=="dd" and 0<int(a[1])<=31:
            self.fecha=self.fecha[0:6]+a[1]
        elif a[0]=="mm" and 0<int(a[1])<=12:
            self.fecha=self.fecha[0:4]+ "/"+a[1]+self.fecha[7::]
        elif a[0]=="aaaa" and len(a[1])==4:
            self.fecha=a[1]+self.fecha[4::]
        elif a[0]=="HH" and a[1]<24:
            self.hora=a[1]+self.hora[2::]
        elif a[0]=="MM" and a[1]<60:
            self.hora=self.hora[0:2]+a[1]+self.hora[4::]
        elif a[0]=="SS" and a[1]<60:
            self.hora=self.hora[0:4]+a[1]
        else:
            print("Configuración no válida")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)   