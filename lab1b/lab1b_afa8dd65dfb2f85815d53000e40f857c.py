sensor1=int(input("temperatura sensor1"))
sensor2=int(input("temperatura sensor2"))
sensor3=int(input("temperatura sensor3"))
if sensor1<=0 or sensor2<=0 or sensor3<=0:
    print("encendido")
    print("encendido")
    print("encendido")
else:
    if(sensor1<=5):
        print("encendido")
    else:
        print("apagado")
       
    if(sensor2<=5):
        print("encendido")
    else:
        print("apagado")
       
    if(sensor3<=5):
        print("encendido")
    else:
        print("apagado")


