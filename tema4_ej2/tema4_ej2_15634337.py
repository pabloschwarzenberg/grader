class Auto:
    def __init__(self, capacidad_estanque,rendimiento):
        self.kilometraje= 0
        self.cuenta_kilometros= 0
        self.capacidad_estanque= capacidad_estanque
        self.nivel_estanque= 0
        self.rendimiento= rendimiento
        #el rendimiento esta en kilometros por litro
    def reiniciar_cuentakilometros(self):
        cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        self.kilometraje=self.kilometraje+distancia
        self.cuenta_kilometros=self.cuenta_kilometros+distancia
        self.nivel_estanque=self.nivel_estanque-(distancia/self.rendimiento)
        if self.nivel_estanque>=0:
            return 0
        else:
            faltaron=(0-self.nivel_estanque)*self.rendimiento
            return faltaron
    def autonomia(self):
        recorrer=self.nivel_estanque*self.rendimiento
        return recorrer
    def llenar_estanque(self,litros):
        q=self.capacidad_estanque-self.nivel_estanque
        if litros>q:
            return (q,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return(self.nivel_estanque,True)
if __name__ == "__main__":
    auto=Auto(100,12)