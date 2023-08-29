class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.kilometraje = 0
        self.rendimiento = rendimiento
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0 # se reinicia cuenta kilometros
        
    def andar(self,velocidad,tiempo):
        self.kilometraje = self.kilometraje + (velocidad*tiempo) #se modifica cantidad de kilometros recorridos
        self.cuenta_kilometros = self.cuenta_kilometros + (velocidad*tiempo)  # se modifica cuenta_kilometros
        self.nivel_estanque = self.nivel_estanque - (velocidad*tiempo)/self.rendimiento #litros que quedan
        if self.nivel_estanque >= 0:
            return 0
        else:
            return(-(self.nivel_estanque*self.rendimiento)) # los km que faltaron
    def autonomia(self):
        return((self.nivel_estanque)*self.rendimiento) #los km que puede recorrer con los litros que tiene
    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque = self.nivel_estanque + litros
            return(self.nivel_estanque+ litros,True)
        else:
            return(self.capacidad_estanque-self.nivel_estanque,False)
    
    def __str__(self):
        self.nivel_estanque = str(self.nivel_estanque) + " l"
        return str(self.capacidad_estanque) + "-" + str(self.kilometraje) + "-" + str(self.rendimiento) + "-" + str(self.cuenta_kilometros) + "-" + str(self.nivel_estanque)
if __name__ == "__main__":
    auto=Auto(60,12)
    b = auto.andar(120,1)
    print(b)
    print(auto)