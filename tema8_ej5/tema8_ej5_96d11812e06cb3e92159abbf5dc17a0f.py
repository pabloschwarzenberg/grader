class FechaHora:
    def __init__(self):
        self.año = 0
        self.mes = 0
        self.dia = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.año,self.mes,self.dia,self.hora,self.minuto,self.segundo)

    def fijarFecha(self,fecha):
        if "-" in fecha:
          char = "-"
        else:
          char = "/"
        
        fecha_lista = fecha.split(char)
        self.dia = fecha_lista[0]
        self.mes = fecha_lista[1]
        self.año = fecha_lista[2]

    def fijarHora(self,hora):
        hora_lista = hora.split(":")
        self.hora = hora_lista[0]
        self.minuto = hora_lista[1]
        self.segundo = hora_lista[2]

    def fijarFechaHora(self,fechahora):
        fechahora_lista = fechahora.split(" ")
        fecha = fechahora_lista[0]
        hora = fechahora_lista[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,parte):
        parte_lista = parte.split("=")
        parte = parte_lista[0].replace(" ", "")
        valor = parte_lista[1]
        if parte == "dd":
            if int(valor) > 31:
                print("El día no puede ser mayor a 31")
            else:
              self.dia = int(valor)
        elif parte == "mm":
          if int(valor) > 12:
            print("El mes no puede ser mayor a 12")
          else:
            self.mes = int(valor)
        elif parte == "aaaa":
          if int(valor) > 9999:
            print("El año no puede ser mayor a 9999")
          else:
            self.año = int(valor)
        elif parte == "HH":
          if int(valor) > 23:
            print("La hora no puede ser mayor a 23")
          else:
            self.hora = int(valor)
        elif parte == "MM":
          if int(valor) > 59:
            print("El minuto no puede ser mayor a 59")
          else:
            self.minuto = int(valor)
        elif parte == "SS":
          if int(valor) > 59:
            print("El segundo no puede ser mayor a 59")
          else:
            self.segundo = int(valor)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)