class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0#va aumentando al usar el auto
        self.cuenta_kilometros=0#cuenta de los kilometros recorridos 
        self.capacidad_estanque=capacidad_estanque#combustible max
        self.nivel_estanque=0#litros  del estanque ,menor o igual a la capacidad maxima
        self.rendimiento=rendimiento# kilometros por litro que rinde el auto
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        self.nivel_estanque=self.nivel_estanque-(velocidad*tiempo*(1/self.rendimiento))
        self.kilometraje=self.kilometraje+velocidad*tiempo
        self.cuenta_kilometros=self.cuenta_kilometros+velocidad*tiempo
        if self.nivel_estanque>=0:
            return 0
        elif self.nivel_estanque<0:
            return -(self.nivel_estanque*self.rendimiento)
    def autonomia(self):
        return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque+=litros
            return(self.nivel_estanque,True)
    

if __name__ == "__main__":
    auto=Auto(100,12)
         