class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        self.velocidad=velocidad
        self.tiempo=tiempo
        self.distancia=velocidad*tiempo
        self.kilometraje+=self.distancia
        self.cuenta_kilometros+=self.distancia
        self.nivel_final=self.nivel_estanque-(self.distancia)/(self.rendimiento)
        if self.nivel_final<0:
            litros_faltantes=nivel_final*(-1)
            distancia_faltante=self.rendimiento*litros_faltantes
            return distancia_faltante
        self.nivel_estanque=self.nivel_final
        
    def autonomia(self):
        puedes_recorrer=self.nivel_estanque*self.rendimiento
        return puedes_recorrer

    def llenar_estanque(self,litros):
        if (self.nivel_estanque+litros)>self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque, True
        
  
if __name__ == "__main__":
    auto=Auto(100,12)
    auto.llenar_estanque(60)
    auto.andar(120,1)