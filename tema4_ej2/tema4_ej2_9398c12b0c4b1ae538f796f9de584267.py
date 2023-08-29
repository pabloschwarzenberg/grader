class Auto:
    def __init__(self, capacidad_estanque, rendimiento,kilometraje=0,cuenta_kilometros=0,nivel_estanque=0):
        self.kilometraje=kilometraje
        self.cuenta_kilometros=cuenta_kilometros
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=nivel_estanque
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,vel,t):
        self.distancia=vel*t
        self.litros_necesarios=self.distancia/self.rendimiento
        self.distancia_que_alcanza_a_recorrer=self.rendimiento*self.nivel_estanque
        if self.distancia_que_alcanza_a_recorrer>=self.distancia:
            self.kilometraje=self.kilometraje+vel*t
            self.cuenta_kilometros=self.cuenta_kilometros+vel*t
            self.nivel_estanque=self.nivel_estanque-self.litros_necesarios
            return 0
        else:
            self.nivel_estanque=0
            km_faltan=(vel*t)-(self.rendimiento*self.nivel_estanque)
            return km_faltan
            
    def autonomia(self):
        self.distancia_que_alcanza_a_recorrer=self.rendimiento*self.nivel_estanque
        return self.distancia_que_alcanza_a_recorrer
        
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros> self.capacidad_estanque:
            self.max_combustible=self.capacidad_estanque-self.nivel_estanque
            return self.max_combustible,False
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return self.nivel_estanque,True
        

if __name__ == "__main__":
    auto=Auto(100,12)
    km_recorrer=int(input("km?"))
    c=0
    while auto.cuenta_kilometros<km_recorrer:
        auto.llenar_estanque
        auto.andar
        c=c+1
    print(c)
         