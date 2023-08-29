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
        litros_necesarios = distancia_recorrida / self.rendimiento
        
        if litros_necesarios <= self.nivel_estanque:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return 0
        else:
            kilometros_faltantes = (self.nivel_estanque * self.rendimiento) - distancia_recorrida
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)
