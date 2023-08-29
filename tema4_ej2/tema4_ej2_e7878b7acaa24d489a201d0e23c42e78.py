class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return ""
    def andar(self,velocidad,tiempo):
        self.cuenta_kilometros+=velocidad*tiempo
        self.kilometraje+=velocidad*tiempo
        litros=(velocidad*tiempo)/self.rendimiento
        self.nivel_estanque-=litros
        if self.nivel_estanque >=0:
            return 0
        else:
            return -(self.nivel_estanque)
        
        
    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros
        
    def llenar_estanque(self,litros):
        if (self.nivel_estanque+litros)>self.capacidad_estanque:
            return self.capacidad_estanque,False
            
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)
         