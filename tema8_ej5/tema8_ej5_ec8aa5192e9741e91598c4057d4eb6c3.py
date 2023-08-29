class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
    
    def fijarFecha(self, fecha_str):
        self.fecha = fecha_str
    
    def fijarHora(self, hora_str):
        self.hora = hora_str
    
    def fijarFechaHora(self, fecha_hora_str):
        self.fecha, self.hora = fecha_hora_str.split()
    
    def cambiar(self, parametro):
        nombre, valor = parametro.split("=")
        nombre = nombre.strip().lower()
        valor = valor.strip()
        
        if nombre == "dd":
            self.fecha = valor + self.fecha[2:]
        elif nombre == "mm":
            self.fecha = self.fecha[:3] + valor + self.fecha[5:]
        elif nombre == "aaaa":
            self.fecha = self.fecha[:6] + valor
        elif nombre == "hh":
            self.hora = valor + self.hora[2:]
        elif nombre == "MM":
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif nombre == "SS":
            self.hora = self.hora[:6] + valor
        else:
            raise ValueError("El parámetro especificado no es válido")
    
    def __str__(self):
        return f"{self.fecha} {self.hora}"
