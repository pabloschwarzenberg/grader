class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje= 0 #todavia no hemos andado nada
      self.cuenta_kilometros= 0 #no partimos, entonces no hay nada que reiniciar
      self.nivel_estanque= 0 #no hemos hechado bencina
      
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros = 0
      
      
    def andar(self, velocidad, tiempo):
      self.velocidad=velocidad
      self.tiempo=tiempo
      
      self.distancia= velocidad/tiempo
      
      self.cuenta_kilometros += self.distancia
      self.kilometraje += self.distancia
      
      if self.nivel_estanque > self.distancia:
        self.nivel_estanque -= self.distancia
        return 0 
        
      else:
        return int(self.distancia) - int(self.nivel_estanque)
        
    def autonomia (self):
      self.autonomia = int(self.nivel_estanque)*int(self.rendimiento)
      return self.autonomia
      
    def llenar_estanque(self, litros_a_poner):
      if int(litros_a_poner) + int(self.nivel_estanque) > int(self.capacidad_estanque):
        print ("{};{}".format(Hola, True)


if __name__ == "__main__":
    auto=Auto(100,12)
         