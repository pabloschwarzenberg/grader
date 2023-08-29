class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        
    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        estanque_inicial = self.nivel_estanque
        self.kilometraje += distancia
        self.cuenta_kilometros += distancia
        self.nivel_estanque -= distancia / self.rendimiento
        if self.nivel_estanque < 0:
            self.nivel_estanque = 0
        if self.nivel_estanque > 0:
            return 0
        else:
            distancia_faltante = distancia - (estanque_inicial * self.rendimiento)
            return distancia_faltante
    
    def autonomia(self):
        distancia = self.nivel_estanque * self.rendimiento
        return distancia
        
    def llenar_estanque(self, cantidad_litros):
        llenado = self.nivel_estanque + cantidad_litros
        if llenado > self.capacidad_estanque:
            tupla = (self.capacidad_estanque, False)
            return tupla
        else:
            self.nivel_estanque += cantidad_litros
            tupla = (self.nivel_estanque, True)
            return tupla
            
if __name__ == "__main__":
    auto=Auto(100,12)
         