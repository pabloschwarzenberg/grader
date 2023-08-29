class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    
    def andar(self, velocidad, tiempo_viaje):
        distancia = velocidad * tiempo_viaje
        litros_consumidos = distancia / self.rendimiento
        if litros_consumidos <= self.nivel_estanque:
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_restante = (self.nivel_estanque * self.rendimiento) - distancia
            self.nivel_estanque = 0
            self.kilometraje += distancia - distancia_restante
            self.cuenta_kilometros += distancia - distancia_restante
            return distancia_restante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros_permitidos = self.capacidad_estanque - self.nivel_estanque
            return max_litros_permitidos, False



mi_auto = Auto(100, 12)


distancia_viaje = 1000  
velocidad_viaje = 60  
tiempo_viaje = distancia_viaje / velocidad_viaje  

paradas_carga = 0  

while distancia_viaje > 0:
    distancia_restante = mi_auto.andar(velocidad_viaje, tiempo_viaje)
    if distancia_restante > 0:
        paradas_carga += 1
        litros_a_cargar, _ = mi_auto.llenar_estanque(mi_auto.autonomia())
        tiempo_viaje = distancia_restante / velocidad_viaje
        distancia_viaje = distancia_restante
    else:
        break

print("Tendrás que detenerte a cargar combustible", paradas_carga, "veces en el viaje.")