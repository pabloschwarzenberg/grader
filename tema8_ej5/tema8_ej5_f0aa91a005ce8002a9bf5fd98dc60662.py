class FechaHora:
    def __init__(self):
        self.dd = 0
        self.mm = 0
        self.aaaa = 0
        self.hh = 0
        self.MM = 0
        self.SS = 0
    def __str__(self):
        return str(self.aaaa) + "/" + str(self.mm) + "/" + str(self.dd) + " " + str(self.hh) + ":" + str(self.MM) +  ":" + str(self.SS) 
    def fijarFecha(self,fecha):
       nume = fecha.split("-")
       self.dd = nume[0]
       self.mm = nume[1]
       self.aaaa = nume[2] 

    def fijarHora(self,hora):
        numes = hora.split(":")
        self.hh = numes[0]
        self.MM = numes[1]
        self.SS = numes[2]
    def fijarFechaHora(self,fechahora):
        lista = fechahora.split(" ")
        fecha = lista[0]
        hora = lista[1]
        self.fijarHora(hora)
        self.fijarFecha(fecha)

    def cambiar(self,parte):
        cambiar = parte.split("=")
        if cambiar[0] == "dd" :
          self.dd = cambiar[1]
        if cambiar[0] == "mm" :
          self.mm = cambiar[1]
        if cambiar[0] == "aaaa " :
          que = parte.split(" = ")
          self.aaaa = que[1]
        
        if cambiar[0] == "hh" :
          self.hh = cambiar[1]
        if cambiar[0] == "MM" :
          self.MM = cambiar[1]
        if cambiar[0] == "SS" :
          self.SS = cambiar[1]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
