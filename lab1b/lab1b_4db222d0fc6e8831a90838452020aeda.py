#Heladas
sensor_uno= int(input("ingresa la temperatura del sensor 1"))
sensor_dos= int(input("ingresa la temperatura del sensor 2"))
sensor_tres= int(input("ingresa la temperatura del sensor 3"))

if(sensor_uno<=0 or sensor_dos<=0 or sensor_tres<=0):
    print("encendido\n"*3)
else:
    if sensor_uno<=5:
        print('encendido')
    elif sensor_uno>5:
        print('apagado')



    if sensor_dos<=5:
        print('encendido')
    elif sensor_dos>5:
        print('apagado')
     

    if sensor_tres<=5:
        print('encendido')
    elif sensor_tres>5:
        print('apagado')