class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo):
        cantidad_kilometros=velocidad*tiempo
        cantidad_litros_necesarios=cantidad_kilometros/self.rendimiento
        if self.nivel_estanque>=cantidad_litros_necesarios:
            self.nivel_estanque=self.nivel_estanque-cantidad_litros_necesarios
            self.cuenta_kilometros=cantidad_kilometros
            return 0
        else:
            r=cantidad_litros_necesarios-self.nivel_estanque
            self.nivel_estanque=0
            return r
    def autonomia(self):
        cantidad_kilometros= self.nivel_estanque*self.rendimiento
        return cantidad_kilometros
        
    def llenar_estanque(self,cantidad_litros):
        if self.capacidad_estanque>=self.nivel_estanque+cantidad_litros:
            self.nivel_estanque= self.nivel_estanque+cantidad_litros
            return(self.nivel_estanque+cantidad_litros,True)
        else:
            return(self.capacidad_estanque,False)
        

if __name__ == "__main__":
    auto=Auto(100,12)
         