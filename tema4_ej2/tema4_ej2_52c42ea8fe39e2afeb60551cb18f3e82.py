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
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.nivel_estanque = 0
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            return distancia_faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


# Ejemplo de uso
auto = Auto(capacidad_estanque=100, rendimiento=12)

velocidad = 80  # km/h
tiempo_viaje = 5  # horas

distancia_total = velocidad * tiempo_viaje
litros_necesarios_total = distancia_total / auto.rendimiento

n_cargas = 0
distancia_restante = distancia_total

while distancia_restante > 0:
    autonomia = auto.autonomia()
    
    if autonomia >= distancia_restante:
        distancia_restante = 0
    else:
        distancia_restante -= autonomia
        litros_carga, _ = auto.llenar_estanque(auto.capacidad_estanque)
        n_cargas += 1

    auto.andar(velocidad, tiempo_viaje)

print("Cantidad de veces que debes detenerte a cargar combustible:", n_cargas)
