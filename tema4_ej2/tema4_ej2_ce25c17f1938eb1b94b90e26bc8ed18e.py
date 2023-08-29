class Auto:
   kilometraje=0
   cuenta_kilometros=0
   capacidad_estanque=0
   nivel_estanque=0
   rendimiento=0
   reiniciar_cuentakilometros=0
   andar=0
   autonomia=0
   llenar_estanque=0
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
         