class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros= 0
        self.capacidad_estanque= capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia= velocidad * tiempo
        litros_gastados= distancia/self.rendimiento
        if litros_gastados > self.nivel_estanque:
            litros_faltantes = litros_gastados - self.nivel_estanque
            self.nivel_estanque = 0
            km_a_recorrer = self.rendimiento * litros_faltantes
            km_recorridos = distancia - km_a_recorrer
            self.kilometraje += km_recorridos
            self.cuenta_kilometros += km_recorridos
            return km_a_recorrer
        else:
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            self.nivel_estanque -= litros_gastados
            return 0

    def autonomia(self):
      return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self,litros):
        if litros+self.nivel_estanque > self.capacidad_estanque:
          posible = self.capacidad_estanque - self.nivel_estanque
          return [posible,False]
         
        else:
          self.nivel_estanque+=litros
          return[self.nivel_estanque,True]
          
if __name__ == "__main__":
    auto = Auto(100, 12)
        
  
         