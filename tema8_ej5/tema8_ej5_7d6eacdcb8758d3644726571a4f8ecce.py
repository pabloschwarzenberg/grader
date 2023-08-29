class FechaHora:
    def __init__(self):
      self.mes = ""
      self.dia = ""
      self.ano = ""
      self.horax = ""

    def __str__(self):
        return("{}/{}/{} {}".format(self.ano,self.mes,self.dia,self.horax))

    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
        self.horax = hora

    def fijarFechaHora(self,fechahora):
        e = fechahora.split(" ")
        self.horax = e[1]
        e.pop(1)
        e = "".join(e)
        e = e.split("-")
        self.ano = e[2]
        self.dia = e[0]
        self.mes = e[1]
       
    def cambiar(self,parte):
        if parte.find("mm")!=-1:
          if parte.split(" ") !=-1:
            l = parte.split(" ")
            l = "".join(parte)
            g = int(l.find("="))
            u = parte[g+1:]
            self.mes = u
          else:
            g = int(l.find("="))
            u = parte[g+1:]
            self.mes = u
              
            
        elif parte.find("aaaa")!=-1:
            if parte.split(" ") !=-1:
                li = parte.split(" ")
                l = "".join(li)
                g = int(l.find("="))
                u = l[g+1:]
                self.ano = u
            else:
                g = int(l.find("="))
                u = parte[g+1:]
                self.ano = u
                

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    print(fh)