class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        if self.cuenta_kilometros !=0:
            self.cuenta_kilometros=0
        else:
            pass
    def autonomia(self):
        self.autonomia=self.rendimiento*self.nivel_estanque
        
    def andar(self,velocidad,tiempo):
        self.velocidad=velocidad
        self.tiempo=tiempo
        self.distancia=self.velocidad * self.tiempo
        self.nivel_estanque=self.nivel_estanque-(self.distancia/self.rendimiento)
        if self.nivel_estanque>=0:
            self.kilometraje=self.kilometraje + self.distancia
            self.cuenta_kilometros=self.cuenta_kilometros + self.distancia
            return 0
        elif self.nivel_estanque< 0:
            self.litros_faltantes=-1*(self.nivel_estanque)
            self.distancia_faltante=self.rendimiento * self.litros_faltantes
            self.distancia=self.autonomia - self.distancia_faltante
            self.kilometraje=self.kilometraje + self.distancia
            self.cuenta_kilometros=self.cuenta_kilometros + self.distancia
            return self.distancia_faltante
            
    def llenar_estanque(self,cantidad_litros):
        self.cantidad_litros=cantidad_litros
        if (cantidad_litros + self.nivel_estanque)> self.nivel_estanque:
            self.max_litros=self.capacidad_estanque - self.nivel_estanque
            return tuple([self.max_litros,False])
         

if __name__ == "__main__":
    auto=Auto(100,12)
         