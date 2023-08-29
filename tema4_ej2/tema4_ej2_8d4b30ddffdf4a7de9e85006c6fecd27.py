class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
    def reiniciar_ceuntakilometros(self):
        self.cuenta_kilometros = 0
        
    def andar(self, velocidad, tiempo):
        self.nivel_estanque -= velocidad * tiempo / self.rendimiento
        self.kilometraje += velocidad * tiempo
        self.cuenta_kilometros += velocidad * tiempo
        
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
        
        
    def llenar_estanque(self,cantidad_litros):
        if self.nivel_estanque + cantidad_litros <= self.capacidad_estanque:
          self.nivel_estanque += cantidad_litros
          return True
          return self.nivel_estanque
        elif self.nivel_estanque + cantidad_litros > self.capacidad_estanque:
          return False
          return self.capacidad_estanque


        

if __name__ == "__main__":
    auto=Auto(100,12)
         