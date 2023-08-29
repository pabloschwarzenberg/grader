class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad=capacidad_estanque
        self.rend=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        self.cuenta_kilometros=0
        self.nivel_estanque-=((self.rend/(velocidad*tiempo))**-1)
        self.kilometraje+=(velocidad*tiempo)
        self.cuenta_kilometros+=(velocidad*tiempo)
    def autonomia(self):
        self.kilometros=self.nivel_estanque*self.rend
        return self.kilometros
    def llenar_estanque(self,litros):
        if self.capacidad>=self.nivel_estanque+litros:
            self.nivel_estanque+=litros
            respuesta=[self.nivel_estanque, True]
        else:
            respuesta=[self.capacidad,False]
        return respuesta
        
        
if __name__ == "__main__":
    auto=Auto(100,12)
         