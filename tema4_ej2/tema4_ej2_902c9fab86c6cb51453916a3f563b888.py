class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento

        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            litros_faltantes = litros_necesarios - self.nivel_estanque
            self.nivel_estanque = 0
            return litros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_permitidos = self.capacidad_estanque - self.nivel_estanque
            return litros_permitidos, False


# Ejemplo de uso
auto = Auto(capacidad_estanque=100, rendimiento=12)

velocidad = 80
tiempo = 4

litros_faltantes = auto.andar(velocidad, tiempo)

if litros_faltantes == 0:
    print("El viaje se completó sin problemas.")
else:
    print(f"Faltaron {litros_faltantes:.2f} litros para completar el viaje.")

paradas_carga = 0

while litros_faltantes > 0:
    litros_permitidos, exito = auto.llenar_estanque(litros_faltantes)
    if exito:
        litros_faltantes -= litros_permitidos
        paradas_carga += 1
    else:
        break

print(f"Deberás detenerte a cargar combustible {paradas_carga} veces en el viaje.")
