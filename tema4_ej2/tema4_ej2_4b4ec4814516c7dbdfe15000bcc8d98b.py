class Auto:
    Autos = []
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        Auto.Autos.append(str(self))

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return
    
    def andar(self,velocidad,tiempo):
        self.distancia=velocidad*tiempo
        self.distancia_maxima=self.rendimiento*self.nivel_estanque
        if self.distancia_maxima>=self.distancia:
           self.kilometraje=self.kilometraje+self.distancia
           self.cuenta_kilometros=self.cuenta_kilometros+self.distancia
           self.nivel_estanque=self.nivel_estanque-(self.distancia/self.rendimiento)
           return 0
        elif self.distancia_maxima<self.distancia:
            x=self.distancia-self.distancia_maxima
            self.kilometraje=self.kilometraje+self.distancia_maxima
            self.cuenta_kilometros=self.cuenta_kilometros+self.distancia_maxima
            self.nivel_estanque=0
            return x
        
    def autonomia(self):
        autonomia=self.rendimiento*self.nivel_estanque
        return autonomia
    
    def llenar_estanque(self,litros):
        self.litros=litros
        if (self.nivel_estanque+self.litros)>self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque=self.nivel_estanque+self.litros
            return (self.nivel_estanque, True)
    def __str__(self):
        return str((self.nivel_estanque, self.kilometraje, self.autonomia()))
    def __lq__(self,other):
        if self.cuanta_kilometros<self.distancia:
            return True
        else:
            return False

    
  

if __name__ == "__main__":
    auto=Auto(100,12)
    auto.llenar_estanque(100)
    auto.andar(100,9)

    litros_necesarios=auto.distancia/auto.rendimiento
    paradas=(litros_necesarios-auto.nivel_estanque)//100

    print(paradas)