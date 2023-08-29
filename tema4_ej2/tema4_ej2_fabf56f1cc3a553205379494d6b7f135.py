class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad=int(capacidad_estanque)
        self.rendimiento=int(rendimiento)
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self, a,b):
        c=int(a)*int(b)
        self.kilometraje+=c
        self.cuenta_kilometros+=c
        self.nivel_estanque-=c/self.rendimiento
        if self.nivel_estanque>=0:
          return 0
        else:
          d=self.nivel_estanque
          self.nivel_estanque=0
          return -1*d*self.rendimiento
    def autonomia(self):
        return int(self.nivel_estanque)*int(self.rendimiento)
    def llenar_estanque(self, litros):
        if self.nivel_estanque+int(litros)<=self.capacidad:        
          self.nivel_estanque+=int(litros)
          return (self.nivel_estanque,True)
        else:
          return (self.capacidad,False)
          
        

if __name__ == "__main__":
    auto=Auto(100,12)
         