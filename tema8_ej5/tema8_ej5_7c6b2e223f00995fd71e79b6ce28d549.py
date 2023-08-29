class FechaHora:
    def __init__(self):
        self.fecha="aaaa/mm/dd"
        self.hora="HH:MM:SS"

    def __str__(self):

        if "-" in self.fecha:
            lista_fecha=self.fecha.split("-")
        if "/" in self.fecha:
            lista_fecha=self.fecha.split("/")

        fecha_str=lista_fecha[2]+"/"+lista_fecha[1]+"/"+lista_fecha[0]
        
        return "{0} {1}".format(fecha_str,self.hora)

    def fijarFecha(self,fecha):
        self.fecha=fecha

    def fijarHora(self,hora):
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        lista=fechahora.split()
        self.fecha=lista[0]
        self.hora=lista[1]

    def cambiar(self,parte):
        parte=parte.replace(" ","")
        cambio=parte.split("=")
        
        if "-" in self.fecha:
            lista_fecha=self.fecha.split("-")
        if "/" in self.fecha:
            lista_fecha=self.fecha.split("/")

        lista_hora=self.hora.split(":")
        
        if cambio[0]=="dd":
            if len(cambio[1])==2:
                lista_fecha[0]=cambio[1]
                
            if len(cambio[1])==1:
                lista_fecha[0]="0"+cambio[1]

            self.fecha="-".join(lista_fecha)
                
        if cambio[0]=="mm":
            if len(cambio[1])==2:
                lista_fecha[1]=cambio[1]
                
            if len(cambio[1])==1:
                lista_fecha[1]="0"+cambio[1]

            self.fecha="-".join(lista_fecha)
            
        if cambio[0]=="aaaa":
            if len(cambio[1])==1:
                lista_fecha[2]="000"+cambio[1]
                
            if len(cambio[1])==2:
                lista_fecha[2]="00"+cambio[1]

            if len(cambio[1])==3:
                lista_fecha[2]="0"+cambio[1]
                
            if len(cambio[1])==4:
                lista_fecha[2]=cambio[1]

            self.fecha="-".join(lista_fecha)
        
        if cambio[0]=="HH":
            if len(cambio[1])==2:
                lista_hora[0]=cambio[1]
                
            if len(cambio[1])==1:
                lista_hora[0]="0"+cambio[1]

            self.hora=":".join(lista_hora)
            
        if cambio[0]=="MM":
            if len(cambio[1])==2:
                lista_hora[1]=cambio[1]
                
            if len(cambio[1])==1:
                lista_hora[1]="0"+cambio[1]

            self.hora=":".join(lista_hora)
        if cambio[0]=="SS":
            if len(cambio[1])==2:
                lista_hora[2]=cambio[1]
                
            if len(cambio[1])==1:
                lista_hora[2]="0"+cambio[1]

            self.hora=":".join(lista_hora)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           