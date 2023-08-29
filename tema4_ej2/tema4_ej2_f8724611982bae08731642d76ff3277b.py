class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    
    def andar(self, velocidad, tiempo):
        km= velocidad*tiempo
        self.cuenta_kilometros += km
        self.kilometraje += km
        litros=km/self.rendimiento
        if litros > self.nivel_estanque:
          litros_faltantes=litros-self.nivel_estanque
          km_restantes=litros_faltantes * self.rendimiento
          return km_restantes
        else:
          self.nivel_estanque -= litros
          return 0
          
    def autonomia(self):
        km=self.nivel_estanque * self.rendimiento
        return km
        
    def llenar_estanque(self, litros):
        a=self.nivel_estanque
        cantidad=a+litros
        if cantidad > self.capacidad_estanque:
          return self.capacidad_estanque, False
        else:
          self.nivel_estanque+=litros
          return self.nivel_estanque, True
    

if __name__ == "__main__":
    auto=Auto(100,12)
    llenadas=0
    viaje=int(input())
    auto.llenar_estanque(100)
    llenadas += 1
    d=auto.autonomia
    
    while viaje>d:
      viaje-=d
      llenadas+=1
      
    auto.andar(100,100/d)
    print(llenadas)
        
        
    
         