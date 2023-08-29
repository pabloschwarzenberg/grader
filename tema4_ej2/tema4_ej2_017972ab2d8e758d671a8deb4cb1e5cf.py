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