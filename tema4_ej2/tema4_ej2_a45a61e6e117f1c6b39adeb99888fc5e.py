class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
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
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return (self.nivel_estanque, True)
        else:
            return (self.capacidad_estanque, False)

if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje_distancia = 500  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio durante el viaje en km/h
    tiempo_viaje = viaje_distancia / velocidad_viaje  # Tiempo total del viaje en horas
    
    num_paradas = 0
    while viaje_distancia > 0:
        resultado = auto.andar(velocidad_viaje, tiempo_viaje)
        if resultado > 0:
            num_paradas += 1
            auto.llenar_estanque(auto.capacidad_estanque)
        viaje_distancia -= auto.cuenta_kilometros
        auto.reiniciar_cuentakilometros()
    
    print("Número de paradas necesarias:", num_paradas)
         