class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        km=velocidad*tiempo
        if km>self.nivel_estanque*self.rendimiento:
            q=km-(self.nivel_estanque*self.rendimiento)
            self.nivel_estanque=0
            return q
        else:
          l=(km)/(self.rendimiento)
          self.nivel_estanque=self.nivel_estanque-l
          return 0

    def autonomia(self):
        km=self.nivel_estanque*self.rendimiento
        return km

    def llenar_estanque(self,litros):
        a=self.nivel_estanque+litros
        if a>self.capacidad_estanque:
            r=self.capacidad_estanque-self.nivel_estanque
            return r,False
        else:
            self.nivel_estanque=a
            return self.nivel_estanque,True
        
     

if __name__ == "__main__":
    auto=Auto(100,12)
         