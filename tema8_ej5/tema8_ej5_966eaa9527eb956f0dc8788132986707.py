class FechaHora:
    def __init__(self):
        self.aaaa = 0000
        self.mm = 00
        self.dd = 00
        self.HH = 00
        self.MM = 00
        self.SS = 00
 
    def __str__(self):
        return self.aaaa+"/"+self.mm+"/"+self.dd+" "+self.HH+":"+self.MM+":"+self.SS
 
    def fijarFecha(self,fecha):
        if "/" in fecha or "-" in fecha:
            if "/" in fecha:
                lista = fecha.split("/")
            elif "-" in fecha:
                lista = fecha.split("-")
            if int(lista[2]) > 0:
                self.aaaa = lista[2]
            else:
                print("Ingrese un año valido")
            if int(lista[1]) < 13 and int(lista[1]) > 0:
                self.mm = lista[1]
            else:
                print("Ingrese un mes valido")
            if int(lista[0]) < 32 and int(lista[0]) > 0:
                self.dd = lista[0]
            else:
                print("Ingrese un dia valido")
        else:
            print("Ingrese un formato correcto")
 
    def fijarHora(self,hora):                               
        lista = hora.split(":")
        self.HH = lista[0]
        self.MM = lista[1]
        self.SS = lista[2]
 
    def fijarFechaHora(self,fechahora):
        lista = fechahora.split()
        self.fijarFecha(lista[0])
        self.fijarHora(lista[1])
 
    def cambiar(self,parte):
        parte = parte.replace(" ","")
        lista = parte.split("=")
        if lista[0] == "aaaa":
            self.aaaa = lista[1]
        elif lista[0] == "mm":
            if int(lista[1]) > 12:
                print("Ingrese un mes valido")
            else:
                self.mm = lista[1]
        elif lista[0] == "dd":
            if int(lista[1]) > 31:
                print("Ingrese un dia valido")
            else:
                self.dd = lista[1]
        elif lista[0] == "HH":
            self.HH = lista[1]
        elif lista[0] == "MM":
            self.MM = lista[1]
        elif lista[0] == "SS":
            self.SS = lista[1]
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
 
    fh.cambiar("mm=10")
    print(fh)
 
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)                        