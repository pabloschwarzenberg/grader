
class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        
    def andar(self,vel,tiempo):
        self.kilometraje += vel*tiempo
        self.cuenta_kilometros += vel*tiempo
        self.nivel_estanque -= vel*tiempo/self.rendimiento
        if self.nivel_estanque >= 0:
            return(0)
        else:
            return abs(self.nivel_estanque*self.rendimiento)

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    
    def llenar_estanque(self,litros):
        if self.capacidad_estanque - (self.nivel_estanque + litros) < 0:
            return self.capacidad_estanque - self.nivel_estanque , False
        else:
            self.nivel_estanque += litros
            return self.nivel_estanque + litros , True