class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.nivel_estanque=0
        self.cuenta_kilometros=0
        
    def autonomia(self):
        self.autonomi=self.rendimiento*self.nivel_estanque
        return self.autonomi
    def andar(self,velocidad,tiempo):
        self.velocidad=velocidad
        self.tiempo=tiempo
        self.distancia=self.tiempo*self.velocidad
        self.kilometraje=self.kilometraje+self.distancia
        self.cuenta_kilometros=self.cuenta_kilometros+self.distancia
        if self.autonomi<self.distancia:
            A=self.distancia-self.autonomi
        else:
            self.nivel_estanque=self.nivel_estanque-(int(self.distancia)/int(self.rendimiento))
            return 0
        self.nivel_estanque=self.nivel_estanque-(int(self.distancia)/int(self.rendimiento))
        return A
    
    def reiniciar_cuenakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
    def __repr__(self):
        return str(self.autonomia)
    def llenar_estanque(self,litros):
        if litros>(self.capacidad_estanque-self.nivel_estanque):
            return (self.capacidad_estanque-self.nivel_estanque,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return (self.nivel_estanque,True)
        
if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto.llenar_estanque(60))
    print(auto.autonomia())
    print(auto.andar(40,30))


         