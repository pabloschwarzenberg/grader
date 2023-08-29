class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""
    
    def __str__(self):
        return self.fecha + " " + self.hora
    
    def fijarFecha(self, fecha):
        self.fecha = fecha
    
    def fijarHora(self, hora):
        self.hora = hora
    
    def fijarFechaHora(self, fechahora):
        fecha_hora = fechahora.split(" ")
        fecha = fecha_hora[0]
        hora = fecha_hora[1]
        fecha_separada = fecha.split("-")
        self.fecha = fecha_separada[2] + "/" + fecha_separada[1] + "/" + fecha_separada[0]
        self.hora = hora
    
    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip()
        valor = valor.strip()
        
        if parametro == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Día inválido")
                return
            fecha_separada = self.fecha.split("/")
            self.fecha = valor + "/" + fecha_separada[1] + "/" + fecha_separada[2]
        elif parametro == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Mes inválido")
                return
            fecha_separada = self.fecha.split("/")
            self.fecha = fecha_separada[0] + "/" + valor + "/" + fecha_separada[2]
        elif parametro == "aaaa":
            fecha_separada = self.fecha.split("/")
            self.fecha = valor + "/" + fecha_separada[1] + "/" + fecha_separada[2]
        elif parametro == "HH":
            if int(valor) < 0 or int(valor) > 23:
                print("Hora inválida")
                return
            hora_separada = self.hora.split(":")
            self.hora = valor + ":" + hora_separada[1] + ":" + hora_separada[2]
        elif parametro == "MM":
            if int(valor) < 0 or int(valor) > 59:
                print("Minuto inválido")
                return
            hora_separada = self.hora.split(":")
            self.hora = hora_separada[0] + ":" + valor + ":" + hora_separada[2]
        elif parametro == "SS":
            if int(valor) < 0 or int(valor) > 59:
                print("Segundo inválido")
                return
            hora_separada = self.hora.split(":")
            self.hora = hora_separada[0] + ":" + hora_separada[1] + ":" + valor
        else:
            print("Parámetro inválido")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    
    fh.cambiar("mm=10")
    print(fh)
    
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)


           