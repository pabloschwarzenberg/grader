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
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento
        
        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque - self.nivel_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)
        else:
            self.nivel_estanque += cantidad_litros
            return (self.nivel_estanque, True)


# Crear un auto con capacidad de estanque de 100 litros y rendimiento de 12 km/l
auto = Auto(100, 12)

# Realizar un viaje con velocidad de 60 km/h y duración de 5 horas
velocidad_viaje = 60
tiempo_viaje = 5
distancia_viaje = velocidad_viaje * tiempo_viaje

# Calcular cuántas veces se debe detener a cargar combustible
detenciones = 0
kilometros_recorridos = 0

while kilometros_recorridos < distancia_viaje and auto.nivel_estanque > 0:
    resultado = auto.andar(velocidad_viaje, tiempo_viaje)
    
    if resultado > 0:
        detenciones += 1
        kilometros_recorridos += distancia_viaje - resultado
    else:
        kilometros_recorridos += distancia_viaje

print("Cantidad de veces que debes detenerte a cargar combustible:", detenciones)
