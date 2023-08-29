class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.lista_1=[]

    def __str__(self):
        return ""

    def fijarFecha(self,fecha):
        lista_1.append(fecha.split("/"))
        for i in lista_1:
          self.lista_1.append("".join(i))
        self.lista_1.reverse()

    def fijarHora(self,hora):
        self.lista_2=hora.split(":")
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        lista_3=fechahora.split(" ")

    def cambiar(self,parte):
        if "dd" or "mm" or "aaaa" in parte:
          if "dd" in parte and int(parte[3])>31:
            print("Oh, no, te has pasado!")
          elif "dd" in parte and int(parte[3])<=31:
            self.lista_1[2]=parte[3]
          elif "mm" in parte and int(parte[3])>12:
            print("Oh no, te has pasado!")
          elif "mm" in parte and int(parte[3])<=12:
            self.lista_1[1]=parte[3]
          elif "aaaa" in parte:
            self.lista_1[0]=parte[3]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           