class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        self.cuenta_kilometros=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self, velocidad, tiempo):
        km_posible=int(self.rendimiento)*int(self.nivel_estanque)
        if int(tiempo)*int(velocidad)<=km_posible:
          self.kilometraje=self.kilometraje+int(tiempo)*int(velocidad)
          self.nivel_estanque=int(self.nivel_estanque)-int(tiempo)*int(velocidad)/self.rendimiento
          self.cuenta_kilometros=self.cuenta_kilometros+int(tiempo)*int(velocidad)
          return 0
        else:
          return int(tiempo)*int(velocidad)-km_posible
    def autonomia(self):
        return int(self.rendimiento)*self.nivel_estanque
    def llenar_estanque(self, litros):
        if int(litros)<=(int(self.capacidad_estanque)-int(self.nivel_estanque)):
            self.nivel_estanque=int(self.nivel_estanque)+int(litros)
            return (str(self.nivel_estanque),True)
        else:
          return (str((int(self.capacidad_estanque)-int(self.nivel_estanque))),False)

         