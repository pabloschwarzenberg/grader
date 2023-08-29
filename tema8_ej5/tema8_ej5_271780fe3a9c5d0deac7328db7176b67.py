class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.año = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    
    def fijarFecha(self, fecha):
        fecha_parts = fecha.split("/")
        if len(fecha_parts) != 3:
            fecha_parts = fecha.split("-")
        
        self.dia = int(fecha_parts[0])
        self.mes = int(fecha_parts[1])
        self.año = int(fecha_parts[2])
    
    def fijarHora(self, hora):
        hora_parts = hora.split(":")
        
        self.hora = int(hora_parts[0])
        self.minuto = int(hora_parts[1])
        self.segundo = int(hora_parts[2])
    
    def fijarFechaHora(self, fecha_hora):
        fecha_hora_parts = fecha_hora.split(" ")
        
        self.fijarFecha(fecha_hora_parts[0])
        self.fijarHora(fecha_hora_parts[1])
    
    def cambiar(self, parametro):
        parametro_parts = parametro.split("=")        
        
        tipo = parametro_parts[0].strip()
        valor = parametro_parts[1].strip()
        
        if tipo == "dd":
            self.dia = int(valor)
        elif tipo == "mm":
            self.mes = int(valor)
        elif tipo == "aaaa":
            self.año = int(valor)
        elif tipo == "HH":
            self.hora = int(valor)
        elif tipo == "MM":
            self.minuto = int(valor)
        elif tipo == "SS":
            self.segundo = int(valor)
        else:
            raise ValueError("Parámetro inválido")
    
    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.año, self.mes, self.dia, self.hora, self.minuto, self.segundo)



