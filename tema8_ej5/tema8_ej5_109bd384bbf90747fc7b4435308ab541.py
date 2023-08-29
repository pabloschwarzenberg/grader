class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None
    
    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = fecha.split("/")
        else:
            print("Error: Formato de fecha incorrecto")
    
    def fijarHora(self, hora):
        if ":" in hora:
            self.hora, self.minuto, self.segundo = hora.split(":")
        else:
            print("Error: Formato de hora incorrecto")
    
    def fijarFechaHora(self, fecha_hora):
        if "/" in fecha_hora and ":" in fecha_hora:
            fecha, hora = fecha_hora.split()
            self.fijarFecha(fecha)
            self.fijarHora(hora)
        else:
            print("Error: Formato de fecha y hora incorrecto")
    
    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        tipo, valor = parametro.split("=")
        if tipo == "dd":
            if int(valor) > 0 and int(valor) <= 31:
                self.dia = valor
            else:
                print("Error: Día inválido")
        elif tipo == "mm":
            if int(valor) > 0 and int(valor) <= 12:
                self.mes = valor
            else:
                print("Error: Mes inválido")
        elif tipo == "aaaa":
            self.anio = valor
        elif tipo == "HH":
            if int(valor) >= 0 and int(valor) < 24:
                self.hora = valor
            else:
                print("Error: Hora inválida")
        elif tipo == "MM":
            if int(valor) >= 0 and int(valor) < 60:
                self.minuto = valor
            else:
                print("Error: Minuto inválido")
        elif tipo == "SS":
            if int(valor) >= 0 and int(valor) < 60:
                self.segundo = valor
            else:
                print("Error: Segundo inválido")
        else:
            print("Error: Parámetro inválido")
    
    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)

# Ejemplo de uso
if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("01/01/2022")
    fecha_hora.fijarHora("12:30:45")
    print(fecha_hora)
    
    fecha_hora.fijarFechaHora("02/02/2023 23:59:59")
    print(fecha_hora)
    
    fecha_hora.cambiar("dd=31")
    fecha_hora.cambiar("mm=12")
    fecha_hora.cambiar("aaaa=2024")
    fecha_hora.cambiar("HH=18")
    fecha_hora.cambiar("MM=45")
    fecha_hora.cambiar("SS=20")
    print(fecha_hora)
    
    fecha_hora.cambiar("dd=40")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("HH=25")
    fecha_hora.cambiar("MM=70")
    fecha_hora.cambiar("SS=80")