class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
       self.kilometraje = 0
       self.capacidad_estanque = capacidad_estanque
       self.rendimiento = rendimiento
       self.nivel_estanque = 0
       self.cuenta_kilometros = 0
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo_de_viaje):
       tiempo_de_viaje=int(tiempo_de_viaje)
       velocidad = int(velocidad)
       viaje = int(velocidad)*int(tiempo_de_viaje)
       capa_auto = int(self.rendimiento)*int(self.nivel_estanque)
       queda= capa_auto-viaje
       queda= queda / self.rendimiento
       self.nivel_estanque = queda
       return self.nivel_estanque
       
    def autonomia(self):
       cuanto_le_queda = int(self.nivel_estanque)*int(self.rendimiento)
       return cuanto_le_queda
    def llenar_estanque(self,litros):
       litros = int(litros)
       Capacidad_actual = int(self.capacidad_estanque)-int(self.nivel_estanque)
       if int(self.nivel_estanque) + litros > int(self.capacidad_estanque):
          return (Capacidad_actual, False)
       else:
          self.nivel_estanque = int(self.nivel_estanque) + litros
          return (self.nivel_estanque, True)
      
if __name__ == "__main__":
    auto=Auto(100,12)
         