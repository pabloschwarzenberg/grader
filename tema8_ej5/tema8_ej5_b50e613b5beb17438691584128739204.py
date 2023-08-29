class FechaHora:
    def __init__(self):
        self.dia = ""
        self.mes = ""
        self.ano = ""
        self.horas = ""
        self.minutos = ""
        self.segundos = ""

    def __str__(self):
        return str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia)+ " " +str(self.horas) + ":" + str(self.minutos) + ":" +str(self.segundos)

    def fijarFecha(self,fecha):
        if "-" in fecha:
            fecha = fecha.split("-")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]
        if "/" in fecha:
            fecha = fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]

    def fijarHora(self,hora):
        hora = hora.split(":")
        self.horas=hora[0]
        self.minutos=hora[1]
        self.segundos=hora[2]

    def fijarFechaHora(self,fechahora):
        a = fechahora.split(" ")
        fecha = a[0]
        hora = a[1]
        if "-" in fecha:
            fecha = fecha.split("-")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]
        if "/" in fecha:
            fecha = fecha.split("/")
            self.dia=fecha[0]
            self.mes=fecha[1]
            self.ano=fecha[2]
            
        hora = hora.split(":")
        self.horas=hora[0]
        self.minutos=hora[1]
        self.segundos=hora[2]
                
    def cambiar(self,parte):
        parte = parte.split("=")
        parte[0]=parte[0].strip()
        parte[1]=parte[1].strip()
        if parte[0]=="dd":
            self.dia=parte[1]
        if parte[0]=="mm":
            self.mes=parte[1]
        if parte[0]=="aaaa":
            self.ano=parte[1]
        if parte[0]=="HH":
            self.horas=parte[1]
        if parte[0]=="MM":
            self.minutos=parte[1]
        if parte[0]=="SS":
            self.segundos=parte[1]        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2080")
    print(fh)