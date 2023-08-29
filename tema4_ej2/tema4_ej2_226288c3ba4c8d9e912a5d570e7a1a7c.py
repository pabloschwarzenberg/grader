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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            return distancia_faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    
    viaje = [
        (100, 2),  # Velocidad: 100 km/h, Tiempo: 2 horas
        (80, 1),   # Velocidad: 80 km/h, Tiempo: 1 hora
        (60, 0.5)  # Velocidad: 60 km/h, Tiempo: 0.5 horas
    ]
    
    detenciones = 0
    
    for velocidad, tiempo in viaje:
        distancia_faltante = auto.andar(velocidad, tiempo)
        
        if distancia_faltante > 0:
            detenciones += 1
            max_litros, _ = auto.llenar_estanque(distancia_faltante / auto.rendimiento)
            auto.andar(velocidad, tiempo)  # Continuar el viaje después de la detención
    
    print("Cantidad de veces que se detuvo a cargar combustible:", detenciones)