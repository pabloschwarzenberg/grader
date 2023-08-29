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
        distancia=velocidad*tiempo
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        litros_necesarios=distancia/self.rendimiento
        if self.nivel_estanque>=litros_necesarios:
            self.nivel_estanque-=litros_necesarios
            return 0
        else:
            km_faltantes=distancia-(self.rendimiento*self.nivel_estanque)
            return km_faltantes
            
    def autonomia(self):
         km=self.rendimiento*self.nivel_estanque
         return km
         
    def llenar_estanque(self,l):
         if self.nivel_estanque+l <= self.capacidad_estanque:
             self.nivel_estanque+=l
             estanque=self.nivel_estanque+l
             return (estanque, True)
         else:
             si=self.capacidad_estanque-self.nivel_estanque
             return (si, False)
             
             
if __name__ == "__main__":
    auto=Auto(100,12)
    
         