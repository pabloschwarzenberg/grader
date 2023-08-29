class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    
    def fijarFecha(self, fecha):
        fecha_parts = fecha.split("/")
        if len(fecha_parts) != 3:
            fecha_parts = fecha.split("-")
        if len(fecha_parts) != 3:
            raise ValueError("Formato de fecha inválido. Debe ser dd/mm/aaaa o dd-mm-aaaa.")
        
        self.dia = int(fecha_parts[0])
        self.mes = int(fecha_parts[1])
        self.anio = int(fecha_parts[2])
    
    def fijarHora(self, hora):
        hora_parts = hora.split(":")
        if len(hora_parts) != 3:
            raise ValueError("Formato de hora inválido. Debe ser HH:MM:SS.")
        
        self.hora = int(hora_parts[0])
        self.minuto = int(hora_parts[1])
        self.segundo = int(hora_parts[2])
    
    def fijarFechaHora(self, fecha_hora):
        fecha_hora_parts = fecha_hora.split(" ")
        if len(fecha_hora_parts) != 2:
            raise ValueError("Formato de fecha y hora inválido. Debe ser dd/mm/aaaa HH:MM:SS.")
        
        self.fijarFecha(fecha_hora_parts[0])
        self.fijarHora(fecha_hora_parts[1])
    
    def cambiar(self, parametro):
        parametro1 = parametro.split("=")
        if len(parametro1) != 2:
            raise ValueError("Formato de cambio inválido. Debe ser 'tipo=valor'.")
        
        t= parametro1[0].strip()
        v = parametro1[1].strip()
        
        if t == "dd":
            self.dia = int(v)
        elif t == "mm":
            self.mes = int(v)
        elif t == "aaaa":
            self.anio = int(v)
        elif t == "HH":
            self.hora = int(v)
        elif t == "MM":
            self.minuto = int(v)
        elif t == "SS":
            self.segundo = int(v)
        else:
            raise ValueError("Tipo de parámetro inválido.")
    
    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)