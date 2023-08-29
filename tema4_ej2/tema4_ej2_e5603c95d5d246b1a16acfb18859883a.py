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
        litros_consumidos = distancia / self.rendimiento
        
        if litros_consumidos <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_consumidos
            return 0
        else:
            distancia_restante = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            self.nivel_estanque = 0
            return distancia - distancia_restante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Programa de ejemplo
auto = Auto(capacidad_estanque=100, rendimiento=12)
viaje = [(80, 2), (60, 3), (70, 1)]  # Lista de tuplas: (velocidad, tiempo)

paradas_carga = 0

for tramo in viaje:
    velocidad, tiempo = tramo
    distancia_restante = auto.andar(velocidad, tiempo)
    
    if distancia_restante > 0:
        paradas_carga += 1
        litros_faltantes, _ = auto.llenar_estanque(distancia_restante / auto.rendimiento)
        auto.andar(velocidad, tiempo)  # Continuar el viaje después de cargar combustible

print("Número de paradas de carga necesarias:", paradas_carga)
