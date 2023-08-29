class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.nivel_estanque=0
        self.cuentakilometros=0
        
    
    def cuenta_kilometros(self,kilometros):
        self.cuentakilometros=self.cuentakilometros+kilometros
        self.kilometraje=self.kilometraje+self.cuentakilometros
        
        
    def reiniciar_cuentakilometros(self):
        self.cuentakilometros=0
        
    def andar(self,velocidad,tiempo):
        kilo=velocidad*tiempo
        l_gastados=kilo/self.rendimiento
        if l_gastados<=self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque-l_gastados
            self.cuenta_kilometros(kilo)
            self.reiniciar_cuentakilometros()
            return 0
        else: 
            a=l_gastados-self.nivel_estanque
            b=self.rendimiento*a
            c=self.rendimiento*self.nivel_estanque
            self.nivel_estanque=0
            self.cuenta_kilometros(c)
            self.reiniciar_cuentakilometros()
            return b
        
        
        
        
    def llenar_estanque(self,litros):
        a=self.nivel_estanque+litros
        b=self.capacidad_estanque-self.nivel_estanque
        if a>self.capacidad_estanque:
            return (b,False)
        else:
            self.nivel_estanque=a
            return (a,True)
    
    def autonomia(self):
        a=self.nivel_estanque*self.rendimiento
        return a

    
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
         