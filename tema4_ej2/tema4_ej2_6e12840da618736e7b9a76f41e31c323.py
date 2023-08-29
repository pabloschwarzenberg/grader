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
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            kilometros_restantes = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (distancia - kilometros_restantes)
            self.cuenta_kilometros += (distancia - kilometros_restantes)
            self.nivel_estanque = 0
            return kilometros_restantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False
         if __name__ == "__main__":
    auto = Auto(100, 12)  # Capacidad del estanque: 100 litros, Rendimiento: 12 km/l
    
    # Simulación de un viaje
    distancia_total = 800  # Distancia total del viaje en kilómetros
    tiempo_total = 10  # Tiempo total del viaje en horas
    
    detenciones = 0  # Contador de detenciones
    
    while distancia_total > 0:
        autonomia_actual = auto.autonomia()
        
        if autonomia_actual >= distancia_total:
            distancia_total = 0
        else:
            distancia_total -= autonomia_actual
            detenciones += 1
            litros_a_cargar, exito = auto.llenar_estanque(auto.capacidad_estanque)
            if not exito:
                distancia_faltante = distancia_total + litros_a_cargar * auto.rendimiento
                distancia_total -= distancia_faltante
    
    print("Número de detenciones requeridas:", detenciones)
