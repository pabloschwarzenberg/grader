#Heladas




sensorA=int(input("Temperatura de la zona A:"))
SensorB=int(input("Temperatura de la Zona B:"))
SensorC=int(input("Temperatura de la zona C:"))
print("La temperatura de la zona A es:", sensorA)
print("La temperatura de la zona B es:", SensorB)
print("La temperatura de la zona C es:", SensorC)
if sensorA<=0 or SensorB<=0 or SensorC<=0:
    print("encendido\n"*3)

else:
    if sensorA<=5:
        print("encendido")
    else:
        print("apagado")



    if SensorB<=5:
        print("encendido")
    else:
        print("apagado")
    if SensorC<=5:
        print("encendido")
    else:
        print("apagado")
