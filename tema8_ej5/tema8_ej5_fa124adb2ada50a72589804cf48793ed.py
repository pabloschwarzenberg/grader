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
        partes = fechahora.split(" ")
        fecha_partes = partes[0].split("-")
        self.fecha = fecha_partes[2] + "/" + fecha_partes[1] + "/" + fecha_partes[0]
        self.hora = partes[1]
    
    def cambiar(self, parte):
        parametros = parte.split("=")
        tipo = parametros[0].strip()
        valor = parametros[1].strip()
        
        if tipo == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Error: Día inválido.")
            else:
                self.fecha = self.fecha[:8] + valor
        elif tipo == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Error: Mes inválido.")
            else:
                self.fecha = self.fecha[:5] + valor + self.fecha[7:]
        elif tipo == "aaaa":
            if int(valor) < 0:
                print("Error: Año inválido.")
            else:
                self.fecha = valor + self.fecha[4:]
        elif tipo == "HH":
            if int(valor) < 0 or int(valor) > 23:
                print("Error: Hora inválida.")
            else:
                self.hora = valor + self.hora[2:]
        elif tipo == "MM":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Minuto inválido.")
            else:
                self.hora = self.hora[:3] + valor + self.hora[5:]
        elif tipo == "SS":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Segundo inválido.")
            else:
                self.hora = self.hora[:6] + valor

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    
    fh.cambiar("mm=10")
    print(fh)
    
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)