class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0 # el kilometraje va aumentando.
        self.cuenta_kilometros=0 #cuenta de los kilómetros recorridos
        self.nivel_estanque=0 # ombustible que actualmente tiene el estanque
        self.capacidad_estanque=capacidad_estanque # capacidad máxima de combustible
        self.rendimiento=rendimiento # cantidad de kilómetros por litro

    def reiniciar_cuentakilometros(self): # Reinicia a 0 el valor del cuenta kilómetro.
        self.cuenta_kilometros=0
        return self.cuenta_kilometros

    def andar(self,velociad,timepo): # actualizar los litros actuales, el kilometraje y el cuenta kilómetros.
        litros=self.nivel_estanque-(velociad/self.rendimiento)
        self.nivel_estanque=litros

        kilometros=velociad/timepo
        self.kilometraje=kilometros
        
        kilometro_por_listro=velociad/self.rendimiento
        if litros<kilometro_por_listro:
            faltante=kilometro_por_listro-litros
            return faltante
        else:
            return 0

    def autonomia(self): # cuantos kilómetros puede recorrer el auto con los litros
        kilometros=self.rendimiento*self.nivel_estanque
        return kilometros

    def llenar_estanque(self,nivel_estanque): # actualiza los litros actuales.
        lleno=self.nivel_estanque+nivel_estanque
        if lleno>self.capacidad_estanque:
            return [self.capacidad_estanque,False]
        else:
            self.nivel_estanque=lleno
            return [self.nivel_estanque , True]

if __name__ == "__main__":
    obj_auto=Auto(100,12)
    print(obj_auto.llenar_estanque(60))