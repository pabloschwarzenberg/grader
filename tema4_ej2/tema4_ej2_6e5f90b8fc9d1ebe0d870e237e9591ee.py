class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.rendimiento=rendimiento
        self.capacidad_estanque=capacidad_estanque
        self.kilometraje=0
        self.nivel_estanque=0
        self.cuenta_kilometros=0

    def reiniciar_cuentakilomentros(self):
        self.cuenta_kilometros=0
    def andar(self,v,t):
        km=v*t
        self.kilometraje+=km
        self.cuenta_kilometros+=km
        if km<= self.nivel_estanque*self.rendimiento:
            self.nivel_estanque+= -(km/self.rendimiento)
            return 0
        if km> self.nivel_estanque*self.rendimiento:
            return (km-self.nivel_estanque*self.rendimiento) 

    def autonomia(self):
        a= self.nivel_estanque*self.rendimiento
        return a
    def llenar_estanque(self,l):
        if l+ self.nivel_estanque> self.capacidad_estanque:
             
            return self.capacidad_estanque , False
        elif l+ self.nivel_estanque<= self.capacidad_estanque:
            self.nivel_estanque+=l
            return l+self.nivel_estanque , True
            
            
if __name__ == "__main__":
    auto=Auto(100,12)
         