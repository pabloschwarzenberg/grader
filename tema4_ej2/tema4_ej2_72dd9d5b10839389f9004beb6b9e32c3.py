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
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - km_faltantes
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return km_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            max_litros = self.capacidad_estanque
            return (max_litros, False)
        else:
            self.nivel_estanque = litros
            return (self.nivel_estanque, True)