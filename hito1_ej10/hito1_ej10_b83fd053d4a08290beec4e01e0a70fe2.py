#Cajero Automático
Intentos = 3
while (Intentos>0):
    Usuario = input("Ingrese Usuario: ")
    Clave = input("Ingrese Clave: ")

    if (Usuario != "10334151"):
        print("Usuario incorrecto")
        Intentos = Intentos-1
    elif (Usuario == "10334151"):
        if (Clave != "1803"):
            Intentos = Intentos-1
            print("Clave incorrecta")
        elif (Clave == "1803"):
            print("Clave correcta")
            A = float(input("Retiro: ")
                if (0<=A<=100000):
                print("Retirado: ",A)
                b = 1000000 - A
                print("Dinero Restante: ",b)
                elif (A > 100000):
                print("Retiro no valido")
if(Intentos == 0):
   print("Tarjeta Bloqueada")    