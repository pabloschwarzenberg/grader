#CLASE AUTO
class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self, velocidad, tiempo):
        distancia_recorrida = velocidad * tiempo
        litros_consumidos = distancia_recorrida / self.rendimiento
        if litros_consumidos <= self.nivel_estanque:
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            self.nivel_estanque -= litros_consumidos
            return 0
        else:
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia_recorrida
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return distancia_faltante
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            litros_posibles = self.capacidad_estanque - self.nivel_estanque
            return litros_posibles, False
auto = Auto(100, 12)
distancia_viaje = 500  
velocidad = 60  
tiempo_viaje = distancia_viaje / velocidad  
num_paradas = 0
distancia_restante = distancia_viaje
while distancia_restante > 0:
    falta_combustible = auto.andar(velocidad, tiempo_viaje)
    if falta_combustible > 0:
        num_paradas += 1
        litros_a_cargar, _ = auto.llenar_estanque(falta_combustible)
        distancia_restante -= litros_a_cargar * auto.rendimiento
    else:
        distancia_restante = 0
print("Cantidad de paradas necesarias:", num_paradas)

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
           