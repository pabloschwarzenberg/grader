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
            distancia_restante = (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            return distancia - distancia_restante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    
    distancia_total = 1000  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_total / velocidad_viaje  # Tiempo del viaje en horas
    
    recorrido_faltante = distancia_total
    paradas = 0
    
    while recorrido_faltante > 0:
        recorrido_faltante -= auto.andar(velocidad_viaje, tiempo_viaje)
        if recorrido_faltante > 0:
            paradas += 1
    
    print("Se necesitan", paradas, "paradas para cargar combustible en el viaje.")