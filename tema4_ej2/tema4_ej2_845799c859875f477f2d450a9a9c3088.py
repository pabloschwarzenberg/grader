class Automovil():
    kilometraje=0
    cuenta_kilometros=0
    capacidad_estanque=0
    nivel_estanque=0
    rendimiento=0
    
    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
       
    def andar(self,velocidad,tiempoviajeenhoras):
        if (self.velocidad / self.tiempoviajeenhoras)/self.rendimiento <= self.nivel_estanque:
            self.nivel_estanque -= (self.velocidad / self.tiempoviajeenhoras)/self.rendimiento
            self.kilometraje += (self.velocidad / self.tiempoviajeenhoras)
            self.cuenta_kilometros += (self.velocidad / self.tiempoviajeenhoras)
        elif km_tras/self.rendimiento >= self.nivel_estanque:
            combustible_falta = (velocidad / tiempoviajeenhoras)/self.rendimiento - self.nivel_estanque
            return combustible_falta
    
    def autonomia(self):
        km_quedan_para_recorrer = self.nivel_estanque * self.rendimiento
        return km_quedan_para_recorrer
    
    def llenar_estanque(self,litrorellenado):
        if self.nivel_estanque+litrorellenado<=self.capacidad_estanque:
            self.nivel_estanque+=litrorellenado
            tupla = (self.nivel_estanque,True)
            return tupla
        elif self.nivel_estanque+litrorellenado>=self.capacidad_estanque:
            litros_quedan_cargar = self.capacidad_estanque - self.nivel_estanque
            tupla = (litros_quedan_cargar,False)
            return tupla