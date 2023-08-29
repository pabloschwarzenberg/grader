class FechaHora:    
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.lista1=["dd","mm","aaaa"]
        self.lista2=["HH","MM","SS"]
    def __str__(self):
        a=self.fecha.split("/")
        a.reverse()
        fecha="/".join(a)
        return(fecha+" "+self.hora)
    def fijarHora(self,string):
        self.hora=string
    def fijarFecha(self,string):
        if("-" in string):
            print("oak")
            string=string.replace("-","/")
            self.fecha=string
        else:
         self.fecha=string
    def fijarFechaHora(self,string):
        a=string.split(" ")        
        self.fijarFecha(a[0])        
        self.hora=a[1]
    def cambiar(self,string):
        string=string.split("=")
        if(string[0] in self.lista1):
            pos=self.lista1.index(string[0])
            print(pos)
            lista=self.fecha.split("/")
            print(lista)
            print(lista[pos])
            lista[pos]=string[1]
            self.fecha="/".join(lista)            
        if(string[0] in self.lista2):
            pos=self.ista2.index(string[0])            
            lista=self.hora.split(":")
            lista[pos]=string[1]
            self.hora=":".join(lista)
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           