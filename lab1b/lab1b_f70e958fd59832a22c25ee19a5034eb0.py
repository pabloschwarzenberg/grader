#Heladas
a=int(input("Ingrese valor 1° sensor: "))
b=int(input("Ingrese valor 2° sensor: "))
c=int(input("Ingrese valor 3° sensor: "))
if(a>0 and b>0 and c>0):
    if((a<=5 and a>0) or (b<=5 and b>0) or (c<=5 and c>0)):
        if (a<=5):
            print("encendido")
            print("apagado")
            print("apagado")
        if (b<=5):
            print("apagado")
            print("encendido")
            print("apagado")
        if (c<=5):
            print("apagado")
            print("apagado")
            print("encendido")
        if (a<=5 and b<=5 and c<=5):
            print("encendido")
            print("encendido")
            print("encendido")

    
if(a<=0 or b<=0 or c<=0):
    print("encendido")
    print("encendido")
    print("encendido")
    
else:
        print("apagado")
        print("apagado")
        print("apagado")