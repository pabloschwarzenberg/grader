#Heladas
sensor1=int(input("temperata zona 1:"))
sensor2=int(input("temperata zona 2:"))
sensor3=int(input("temperata zona 3:"))
print("la temperatura de la zona 1 es:",sensor1)
print("la temperatura de la zona 2 es:",sensor2)
print("la temperatura de la zona 3 es:",sensor3)
if sensor1<=0 or sensor2<=0 or sensor3<=0:
    print("encendido\n"*3)
else:
    if sensor1<=5:
        print("encendido")
    else:
        print("apagado")
    if sensor2<=5:
        print("encendido")
    else:
        print("apagado")    
    if sensor3<=5:
        print("encendido")
    else:
        print("apagado")
          
          