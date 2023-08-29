class FechaHora:
    def __init__(self, fecha="", hora=""):
        self.dia = ""
        self.mes = ""
        self.anio = ""
        self.hora = ""
        self.minuto = ""
        self.segundo = ""
        
        if fecha:
            self.fijarFecha(fecha)
            
        if hora:
            self.fijarHora(hora)
    
    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = fecha.split("/")
        elif "-" in fecha:
            self.dia, self.mes, self.anio = fecha.split("-")
    
    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = hora.split(":")
    
    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)
    
    def cambiar(self, parametro):
        if "=" in parametro:
            clave, valor = parametro.split("=")
            clave = clave.strip()
            valor = valor.strip()
            
            if clave == "dd":
                if int(valor) > 0 and int(valor) <= 31:
                    self.dia = valor
                else:
                    print("Día inválido.")
            elif clave == "mm":
                if int(valor) > 0 and int(valor) <= 12:
                    self.mes = valor
                else:
                    print("Mes inválido.")
            elif clave == "aaaa":
                self.anio = valor
            elif clave == "HH":
                if int(valor) >= 0 and int(valor) <= 23:
                    self.hora = valor
                else:
                    print("Hora inválida.")
            elif clave == "MM":
                if int(valor) >= 0 and int(valor) <= 59:
                    self.minuto = valor
                else:
                    print("Minuto inválido.")
            elif clave == "SS":
                if int(valor) >= 0 and int(valor) <= 59:
                    self.segundo = valor
                else:
