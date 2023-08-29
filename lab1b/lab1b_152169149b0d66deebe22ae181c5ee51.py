# Siembra de proteccion de heladas.

#sensores.
temperatura_sensor1 = input("ingrese la temperatura captada por el sensor 1: ")
temperatura_sensor2 = input("ingrese la temperatura captada por el sensor 2: ")
temperatura_sensor3 = input("ingrese la temperatura captada por el sensor 3: ")

#verificacion de int.
try:
    temperatura_sensor1 = int(temperatura_sensor1)
    temperatura_sensor2 = int(temperatura_sensor2)
    temperatura_sensor3 = int(temperatura_sensor3)
except ValueError:
    print("los valores ingresados no son numeros.")

#temperatura en alguno menor igual a 0
if temperatura_sensor1 > 0 and temperatura_sensor2 > 0 and temperatura_sensor3 > 0:
    #temperatura menor o igual a 5 grados.
    #temperatura de sensor 1.
    if temperatura_sensor1 <= 5:
        print("encendido")
    else:
        print("apagado")

    #temperatura de sensor 2.
    if temperatura_sensor2 <= 5:
        print("encendido")
    else:
        print("apagado")

    #temperatura de sensor 3.
    if temperatura_sensor3 <= 5:
        print("encendido")
    else:
        print("apagado")
#temperatura en alguno igual a 0
elif temperatura_sensor1 == 0 or temperatura_sensor2 == 0 or temperatura_sensor3 == 0:
    print("encendido")
    print("encendido")
    print("encendido")
else:
    print("encendido")
    print("encendido")
    print("encendido")