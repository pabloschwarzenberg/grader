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
    
    def validar_valor(self, valor, limite_inferior, limite_superior, mensaje):
        valor = int(valor)
        if valor < limite_inferior or valor > limite_superior:
            print(mensaje)
            return False
        return True
    
    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip()
        valor = valor.strip()
        
        if parametro == "dd":
            if not self.validar_valor(valor, 1, 31, "Día inválido"):
                return
            fecha_separada = self.fecha.split("/")
            self.fecha = valor + "/" + fecha_separada[1] + "/" + fecha_separada[2]
        elif parametro == "mm":
            if not self.validar_valor(valor, 1, 12, "Mes inválido"):
                return
            fecha_separada = self.fecha.split("/")
            self.fecha = fecha_separada[0] + "/" + valor + "/" + fecha_separada[2]
        elif parametro == "aaaa":
            if not self.validar_valor(valor, 0, 9999, "Año inválido"):
                return
            fecha_separada = self.fecha.split("/")
            self.fecha = valor + "/" + fecha_separada[1] + "/" + fecha_separada[2]
        elif parametro == "HH":
            if not self.validar_valor(valor, 0, 23, "Hora inválida"):
                return
            hora_separada = self.hora.split(":")
            self.hora = valor + ":" + hora_separada[1] + ":" + hora_separada[2]
        elif parametro == "MM":
            if not self.validar_valor(valor, 0, 59, "Minuto inválido"):
                return
            hora_separada = self.hora.split(":")
            self.hora = hora_separada[0] + ":" + valor + ":" + hora_separada[2]
        elif parametro == "SS":
            if not self.validar_valor(valor, 0, 59, "Segundo inválido"):
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
