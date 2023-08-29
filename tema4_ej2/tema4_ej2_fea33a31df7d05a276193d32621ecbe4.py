class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
       
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo):
        km=velocidad*tiempo
        litros=km/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-litros
        self.kilometraje=self.kilometraje+km
        self.cuenta_kilometros=self.cuenta_kilometros+km
        if self.nivel_estanque>0:
           return True
        
    def autonomia(self):
        a=self.nivel_estanque*self.rendimiento
        return a
        
    def llenar_estanque(self,cantidad_litros):
        if self.nivel_estanque+cantidad_litros<=self.capacidad:
           self.nivel_estanque=self.nivel_estanque+cantidad_litros
           return (self.nivel_estanque,True)
        else: 
           b=(self.nivel_estanque+cantidad_litros)-self.capacidad
           return (b,False)
        

if __name__ == "__main__":
    auto=Auto(100,12)
         