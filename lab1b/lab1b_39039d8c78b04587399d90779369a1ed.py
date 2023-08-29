Sa= int(input("ingrese temperatura sensor 1: "))
Sb= int(input("ingrese temperatura sensor 2: "))
Sc= int(input("ingrese temperatura sensor 3: "))
if (Sa<=0):
    print ("encendido")
    print ("encendido")
    print ("encendido")
elif (Sb<=0):
    print ("encendido")
    print ("encendido")
    print ("encendido")
elif (Sc<=0):
    print ("encendido")
    print ("encendido")
    print ("encendido")
elif(Sa<=5):
    print("encendido")
    if (Sb<=5):
        print("encendido")
        if(Sc<=5):
            print("encendido")
        elif(Sc>5):
            print("apagado")
    elif(Sb>5):
        print("apagado")
        if(Sc<=5):
            print("encendido")
        elif(Sc>5):
            print ("apagado")
elif (Sa <= 5):
    print ("encendido")
    print ("apagado")
    print ("apagado")
elif (Sb<= 5):
    print ("apagado")
    print ("encendido")
    print ("apagado")
elif (Sc<= 5):
    print ("apagado")
    print ("apagado")
    print ("encendido")
elif (Sa>5):
    print ("apagado")
    print ("apagado")
    print ("apagado")
elif (Sb>5):
    print ("apagado")
    print ("apagado")
    print ("apagado")
elif (Sc>5):
    print ("apagado")
    print ("apagado")
    print ("apagado")
