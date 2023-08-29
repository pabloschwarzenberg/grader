sensor1=int(input("temperatura 1er sensor:"))
sensor2=int(input("temperatura 2do sensor:"))
sensor3=int(input("temperatura 3er sensor:"))

            

if sensor1<=0 or sensor2<=0 or sensor3<=0:
    print("encendido\n"*3)

else:
    if sensor1<=5:
        print("encendido")
    else:
        print("apagado")

                

    if sensor2==5 or sensor2==4 or sensor2==3 or sensor2==2 or sensor2==1:
        print("encendido")
    else:
        print("apagado")

                

    if sensor3==5 or sensor3==4 or sensor3==3 or sensor3==2 or sensor3==1:
        print("encendido")
    else:
        print("apagado")





