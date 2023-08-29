#Heladas
 
sensor1= int(input("temperatura actual(s1): "))
sensor2= int(input("temperatura actual(s2): "))
sensor3= int(input("temperatura actual(s3): "))

if sensor1<=5 or sensor2<=0 or sensor3<=0:
    print("encendido")
else:
    print("apagado")


if sensor2<=5 or sensor1<=0 or sensor3<=0:
    print("encendido")
else:
    print("apagado")



if sensor3<=5 or sensor1<=0 or sensor2<=0:
    print("encendido")
else:
    print("apagado")

