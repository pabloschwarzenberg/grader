#CLASE FECHAHORA
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
        parametro_parts = parametro.split("=")
        if len(parametro_parts) != 2:
            raise ValueError("Formato de cambio inválido. Debe ser 'tipo=valor'.")
        
        tipo = parametro_parts[0].strip()
        valor = parametro_parts[1].strip()
        
        if tipo == "dd":
            self.dia = int(valor)
        elif tipo == "mm":
            self.mes = int(valor)
        elif tipo == "aaaa":
            self.anio = int(valor)
        elif tipo == "HH":
            self.hora = int(valor)
        elif tipo == "MM":
            self.minuto = int(valor)
        elif tipo == "SS":
            self.segundo = int(valor)
        else:
            raise ValueError("Tipo de parámetro inválido.")
    
    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)