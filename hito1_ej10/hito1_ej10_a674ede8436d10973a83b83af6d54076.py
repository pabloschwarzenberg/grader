#Cajero Automático
Intentos = 3
while (Intentos>0):
    Usuario = input("Ingrese usuario: ")
    Clave = input("Ingrese contraseña: ")
    
    if (Usuario != "10334151"):
        print("Usuario incorrecto")
        Intentos = Intentos-1
    elif (Usuario == "10334151"):
        if (Clave != "1803"):
            Intentos = Intentos-1
            print("Contraseña incorrecta")
        elif (Clave == "1803"):
            print("Clave aceptada")
            A = float(input("Monto a retirar: "))
            if (0<=A<=100000):
                print("Retirado: ",A)
                b = 1000000 - A
                c = 100000 - A
                print("Saldo cajero= ",b)
                print("Saldo cuenta= ",c)
                break
            elif (A > 100000):
                print("Monto no permitido")
                
if (Intentos == 0):
    print("Tarjeta bloqueada")