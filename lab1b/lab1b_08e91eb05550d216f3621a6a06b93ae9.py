#Heladas
print("Ingrese las temperaturas marcadas por cada sensor\n")
sensor_1 = int(input("\tingrese la temperatura sensor 1: "))
sensor_2 = int(input("\tingrese la temperatura sensor 2: "))
sensor_3 = int(input("\tingrese la temperatura sensor 3: "))
print("\n")

def condicion_1(s): #Si un sensor mide una temperatura menor o igual a 5 grados, se activa el calefactor asociado a ese sensor.
    if s <= 5:
        print("encendido")
    else:
        print("apagado")
def condicion_2(s1, s2, s3): #Si cualquier sensor mide una temperatura igual o menor a 0 grados, se activan los tres calefactores.
    if (s1 <= 0 or s2 <= 0 or s3 <= 0):
        return True
    else:
        return False
print("Estado de los calefactores\n")
if (condicion_2(sensor_1, sensor_2, sensor_3)):
    i = 0
    while i < 3:
        print("encendido")
        i+=1
else:
    condicion_1(sensor_1)
    condicion_1(sensor_2)
    condicion_1(sensor_3)