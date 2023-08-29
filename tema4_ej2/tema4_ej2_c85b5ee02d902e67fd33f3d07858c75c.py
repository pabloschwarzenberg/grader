class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
auto = Auto(100, 12)  # Estanque de 100 litros y rendimiento de 12 km/l

velocidad = 80  # km/h
tiempo = 5  # horas
distancia_viaje = velocidad * tiempo

viajes_detenidos = 0

while distancia_viaje > 0:
    distancia_faltante = auto.andar(velocidad, tiempo)
    if distancia_faltante > 0:
        viajes_detenidos += 1
        litros_a_cargar, _ = auto.llenar_estanque(auto.capacidad_estanque)
        distancia_viaje -= distancia_faltante
    else:
        distancia_viaje = 0

print("Cantidad de veces detenidas a cargar combustible:", viajes_detenidos)

