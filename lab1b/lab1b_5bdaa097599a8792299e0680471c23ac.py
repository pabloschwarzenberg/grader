#Heladas
temperatura=5

sensor1=int(input("ingresa el sensor1"))
sensor2=int(input("ingresa el sensor2"))
sensor3=int(input("ingresa el sensor3"))
if(sensor1<=0 or sensor2<=0 or sensor3<=0):
    print("encendido\n"*3)
else:    
    if sensor1<=temperatura:
        print('encendido')
    else:
        print('apagado')


    if sensor2<=temperatura:
        print('encendido')
    else:
        print('apagado')


    if sensor3<=temperatura:
        print('encendido')
    else:
        print('apagado')
