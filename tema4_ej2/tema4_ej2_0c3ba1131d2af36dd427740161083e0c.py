class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return
    def andar(self,velocidad,tiempo_de_viaje):
        km_a_recorrer=velocidad*tiempo_de_viaje
        cuanto_recorre=self.rendimiento*self.nivel_estanque
        if km_a_recorrer>cuanto_recorre:
            cuanto_falta=km_a_recorrer-cuanto_recorre
            self.nivel_estanque=0
            return cuanto_falta
        if km_a_recorrer<=cuanto_recorre:
            litros_gastados=(self.nivel_estanque*km_a_recorrer)//cuanto_recorre
            self.nivel_estanque=self.nivel_estanque-litros_gastados
            return 0
            
        self.kilometraje=km_recorridos
        self.cuenta_kilometraje=km_recorridos
    def autonomia(self):
        cuanto_recorre=self.rendimiento*self.nivel_estanque
        return cuanto_recorre
    def llenar_estanque(self,cant_litros):
        if cant_litros>self.capacidad_estanque:
            return self.capacidad_estanque,False
        else:
            self.nivel_estanque +=cant_litros
            if self.nivel_estanque>self.capacidad_estanque:
                self.nivel_estanque = self.nivel_estanque-cant_litros
                return self.capacidad_estanque,False
            else:
                return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)
         