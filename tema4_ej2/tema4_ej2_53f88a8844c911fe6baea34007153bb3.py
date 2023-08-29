class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.kilometraje=0
        
    def setKilometraje(self,kilometraje):
        self.kilometraje=kilometraje
    def setCuenta_kilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=cuenta_kilometros
    def setNivel_estanque(self,nivel_estanque):
        self.nivel_estanque=nivel_estanque
    def reiniciar_cuentakilometro(self):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        nivel_estanquef=self.nivel_estanque-(distancia/self.rendimiento)
        if nivel_estanquef<0:
            setCuenta_kilometros(self.nivel_estanque*self.rendimiento)
            return (distancia-self.nivel_estanque*self.rendimiento)
        else:
            self.setNivel_estanque(nivel_estanquef)
            return 0

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    
    def llenar_estanque(self,litros):
        litrosf=int(self.nivel_estanque)+int(litros)
        if litrosf>self.capacidad_estanque:
            return (self.capacidad_estanque-self.nivel_estanque),False
        else:
            self.setNivel_estanque(litrosf)
            return (litrosf),True

if __name__ == "__main__":
    auto=Auto(100,12)
         
