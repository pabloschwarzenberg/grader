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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return distancia_faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


# Ejemplo de uso
auto = Auto(100, 12)

viaje = [
    (100, 2),  # Velocidad: 100 km/h, Tiempo: 2 horas
    (80, 3),   # Velocidad: 80 km/h, Tiempo: 3 horas
    (120, 1),  # Velocidad: 120 km/h, Tiempo: 1 hora
    (90, 4)    # Velocidad: 90 km/h, Tiempo: 4 horas
]

paradas = 0

for velocidad, tiempo in viaje:
    distancia_faltante = auto.andar(velocidad, tiempo)
    if distancia_faltante > 0:
        paradas += 1
        litros_necesarios = distancia_faltante / auto.rendimiento
        max_litros, _ = auto.llenar_estanque(litros_necesarios)
        print(f"Deteniéndose a cargar combustible. Máxima cantidad de litros permitidos: {max_litros}")
    
print(f"Paradas realizadas: {paradas}")
