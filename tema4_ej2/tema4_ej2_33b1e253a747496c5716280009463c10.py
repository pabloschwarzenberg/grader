class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento # Kilometros por litro que rinde el auto
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    
    def andar(self, velocidad, tiempo):
        distancia_recorrida = velocidad * tiempo
        autonomia = self.rendimiento * self.nivel_estanque
        if distancia_recorrida > autonomia:
            self.nivel_estanque = 0
            self.cuenta_kilometros += autonomia
            self.kilometraje += autonomia
            return distancia_recorrida-autonomia
        else:
            self.nivel_estanque -= distancia_recorrida/self.rendimiento
            self.cuenta_kilometros += distancia_recorrida
            self.kilometraje += distancia_recorrida 
            return 0
    
    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self, litros):
        if litros+self.nivel_estanque > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)

if __name__ == "_main_":
    auto=Auto(100,12)