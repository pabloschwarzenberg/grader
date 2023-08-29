class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def llenar_estanque(self, cantidad_litros):
        a=(self.nivel_estanque+cantidad_litros)

        if a<=self.capacidad_estanque:
            self.nivel_estanque=(self.nivel_estanque+cantidad_litros)
            b=list(str(a))
            b.append(True)  
            return tuple(b)
        else:
            b=list(str(self.capacidad_estanque))
            b.append(False)
            return tuple(b)
    
    def andar(self, tiempo_viaje,velocidad):
        kilometros=velocidad*tiempo_viaje
        self.kilometraje+=kilometros
        self.cuenta_kilometros+=kilometros
        
        combustible_necesario=kilometros/self.rendimiento
        self.nivel_estanque-=combustible_necesario
        
        if Auto.autonomia(self) <= kilometros:
            return 0
        else:
            b= Auto.autonomia(self) - kilometros
            return b


    def autonomia(self):
        a=self.rendimiento*self.nivel_estanque
        return a
        
    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometro=0


if __name__ == "__main__":
    auto=Auto(100,12)
         