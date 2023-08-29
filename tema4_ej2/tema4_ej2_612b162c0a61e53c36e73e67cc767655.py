class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
        
    def andar(self,velocidad,tiempo):
        distancia=(int(velocidad)*int(tiempo))
        #litros= float(distancia/12)
        self.nivel_estanque=self.nivel_estanque-(distancia/self.rendimiento)
        self.kilometraje= self.kilometraje + distancia
        self.cuenta_kilometros=distancia
        if self.nivel_estanque >= 0:
            km_faltan=0
            return km_faltan
        else:
            km_faltan=(-self.nivel_estanque*self.rendimiento)
            return km_faltan
        
    def autonomia(self):
        km_disponibles=(self.nivel_estanque*self.rendimiento)
        return km_disponibles
       
    def llenar_estanque(self,cantidad):
        if cantidad > self.capacidad_estanque:
            x=(self.capacidad_estanque,False)
            return x
        else:
            self.nivel_estanque=cantidad
            x=(cantidad,True)
            return x
              

if __name__ == "__main__":
    auto=Auto(100,12)
         

         