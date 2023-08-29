class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.nivel_estanque= 0
      self.kilometraje = 0
      self.cuenta_kilometros = 0
  def __str__(self):
    return f'Automóvil con capacidad de estanque: {self.capacidad_estanque} litros  y rendimiento de: {self.rendimiento} kms/l'
  
  def get_capacidad_estanque(self):
    return self.capacidad_estanque
  
  def mostrar_cuentaKms(self):
    print(f'Los Kms recorrido es este viaje son: {self.cuenta_kilometros}')
  
  def llenar_estanque(self, cantidad_litros):
    capacidad_max=self.get_capacidad_estanque()
    nivel_actual=self.nivel_estanque
    litros_actuales=self.nivel_estanque+cantidad_litros
    if litros_actuales<= capacidad_max:
      self.nivel_estanque=litros_actuales
      return self.nivel_estanque, True
    else:
      return capacidad_max-nivel_actual, False
  def andar (self, velocidad, tiempo_viaje):
    nivel_actual_combustible=self.nivel_estanque
    kms_max_recorrer=velocidad*tiempo_viaje
    kms_rendimiento=nivel_actual_combustible*self.rendimiento
    kms_faltantes=kms_max_recorrer-kms_rendimiento
    if kms_faltantes > 0:
      return kms_faltantes
    else:
      self.nivel_estanque=nivel_actual_combustible-(kms_rendimiento/self.rendimiento)
      self.kilometraje= self.kilometraje+kms_rendimiento
      self.cuenta_kilometros=self.cuenta_kilometros+kms_rendimiento
      return 0
  

auto1=Auto(100,12)
print(auto1)
#Cambie todo este código, de manera de crear un código nuevo que permita
#crea un programa que te indique cuántas veces tendrás que detenerte a cargar combustible en un determinado viaje, el viaje requiere señalar velocidad, tiempo y carga inicial de combustible
auto1.mostrar_cuentaKms()
combustible, valor=auto1.llenar_estanque(70)
if valor==True:
  print(f'El automóvil ha cargado {combustible} para viaje' )
else:
  print(f'Sólo puede ingresar {combustible} litros de combustible, antes de llenar el estanque ')
logro=auto1.andar(90,2)
if logro ==0:
  print('El viaje ha sido un éxito')
  auto1.mostrar_cuentaKms()
else:
  print(f'Quedan por recorrer {logro} kms. ')
    