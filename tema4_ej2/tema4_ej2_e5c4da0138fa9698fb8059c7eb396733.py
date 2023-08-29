class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros  = 0
    def andar(self, velocidad, tiempo_viaje):
        distancia = velocidad * tiempo_viaje
        if distancia < self.autonomia():
          return distancia-self.autonomia()
        else:
          self.nivel_estanque-=(velocidad//self.rendimiento)
          self.kilometraje +=distancia
          self.cuenta_kilometros+=distancia
          return 0
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    def llenar_estanque(self, litros):
        if self.capacidad_estanque < self.nivel_estanque + litros:
          return (self.capacidad_estanque,False)
        self.nivel_estanque += litros
        return (self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         