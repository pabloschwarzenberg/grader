class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
        self.cuenta_kilometros=0
        self.kilometraje=0

    def reiniciar_cuentakilometros(self):
        self.cuentakilometros=0
        return self.cuentakilometros
    
    def andar(self,velocidad,tiempo):
        nivel_estanque= self.nivel_estanque-(velocidad*tiempo/self.rendimiento)
        self.nivel_estanque=nivel_estanque
        kilometraje=velocidad*tiempo
        self.kilometraje+=kilometraje
        if self.nivel_estanque>=0:
            return 0
        else:
            self.nivel_estanque=0
            return 0
            
    def autonomia(self):
        aut=self.rendimiento*self.nivel_estanque
        return aut
        
    def llenar_estanque(self,litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+litros
            e=(self.nivel_estanque, True)
            return e
        else:
            e=(self.capacidad_estanque - self.nivel_estanque, False)
            return e

if __name__ == "__main__":
    auto=Auto(100,12)
         