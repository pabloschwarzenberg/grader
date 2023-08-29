class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_km=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuenta_km(self):
        self.cuenta_km=0

    def llenar_estanque(self,llenar):
        if self.nivel_estanque+llenar<=(self.capacidad_estanque):
            self.nivel_estanque=self.nivel_estanque+llenar
            return (self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque,False)

    def autonomia(self):
        capaz=self.rendimiento*int(self.nivel_estanque)
        return capaz


    def andar(self,velocidad,tiempo_viaje):
        distancia=velocidad*tiempo_viaje
        km_recorridos=self.rendimiento*self.nivel_estanque
        self.kilometraje+=km_recorridos
        self.cuenta_km=km_recorridos
        litros_consumidos=km_recorridos/self.rendimiento

        
        if km_recorridos>distancia:
            litros_consumidos=distancia/self.rendimiento
            self.kilometraje+=distancia
            self.cuenta_km=distancia
            self.nivel_estanque=self.nivel_estanque-litros_consumidos
            return self.nivel_estanque
        else:
            self.nivel_estanque=self.nivel_estanque-litros_consumidos
            return distancia-km_recorridos


        
if __name__ == "__main__":
    auto=Auto(100,12)
         
