intentos = 3
while (intentos>0):
    usuario= input("ingrese nombre de usuario: ")
    if(usuario != "10334151"):
        print("usuario incorrecto")
        intentos = intentos-1
    elif(usuario == "10334151"):
        clave = input("ingrese contraseña: ")
        if(clave != "1803"):
            intentos = intentos-1
            print ("contraseña incorrecta")
        elif(clave == "1803"):
            M = int(input("Monto a retirar: "))
            if (0<=M<=100000):
                C = 1000000 - M
                S = 100000 - M
                print ("saldo cuenta= ",S)
                print ("saldo cajero= ",C)
                break
            elif (M>100000):
                print("saldo insuficiente")                
if (intentos == 0):
    print ("trajeta blqueada")