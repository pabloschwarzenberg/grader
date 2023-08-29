a1=int(input("La temperatura dentro de la zona uno de la plantacion es: "))
a2=int(input("La temperatura dentro de la zona dos de la plantacion es: "))
a3=int(input("La temperatura dentro de la zona tres de la plantacion es: "))
if(a1<=0):
    print("encendido")
    print("encendido")
    print("encendido")
elif(a2<=0):
    print("encendido")
    print("encendido")
    print("encendido")
elif(a3<=0):
    print("encendido")
    print("encendido")
    print("encendido")
elif(a1<=5):
    print("encendido")
    if(a2<=5):
        print("encendido")
        if(a3<=5):
            print("encendido")
        elif(a3>5):
            print("apagado")
    elif(a2>5):
        print("apagado")
        if(a3<=5):
            print("encendido")
        elif(a3>5):
            print("apagado")
elif(a2<=5):
    print("apagado")
    print("encendido")
    if(a3<=5):
        print("encendido")
    elif(a3>5):
        print("apagado")
elif(a3<=5):
    print("apagado")
    print("apagado")
    print("encendido")
elif(a3>5):
    print("apagado")
    print("apagado")
    print("apagado")

      