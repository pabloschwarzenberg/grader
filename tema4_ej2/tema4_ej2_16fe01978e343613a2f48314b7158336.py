class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.nivel_estanque = 0
        self.kilometraje = 0
        self.cuenta_kilometros = 0
    
    def andar(self,velocidad,tiempo):
        distancia = velocidad * tiempo
        self.kilometraje = self.kilometraje + distancia
        self.cuenta_kilometros = self.cuenta_kilometros + distancia
        gasto = (distancia/self.rendimiento)
        if self.nivel_estanque - gasto<=0:
            faltan = (gasto-self.nivel_estanque)*self.rendimiento
            return faltan
        else:
            self.nivel_estanque = self.nivel_estanque - gasto
            return 0
    
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros = 0
            
    def autonomia(self):
        autonomia_kilometros = self.nivel_estanque * self.rendimiento
        return autonomia_kilometros
    
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros>self.capacidad_estanque:
            return (self.capacidad_estanque-self.nivel_estanque,False)
        else:
            self.nivel_estanque = self.nivel_estanque + litros
            return(self.nivel_estanque,True)
    

if __name__ == "__main__":
    auto=Auto(100,12)

    