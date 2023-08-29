class Auto:
    kilometraje=0
    cuenta_kilometros=0
    nivel_estanque=0

    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        kilometraje=0
        self.kilometraje=0
        return self.kilometraje
        

    def andar(self,velocidad,tiempo):
        kilometros_rec= velocidad * tiempo
        kilometraje=kilometros_rec* self.rendimiento
        self.kilometraje=kilometraje
        self.rendimiento=12
        self.nivel_estanque=50
        return self.kilometraje,self.rendimiento,self.nivel_estanque

    def llenar_estanque(self,litros):
        x=self.nivel_estanque+litros
        if self.capacidad_estanque>x:
            self.nivel_estanque=self.nivel_estanque+litros
            return self.nivel_estanque
    def autonomia(self):
        x=self.rendimiento*self.nivel_estanque
        return x
    


         
         
 
 
