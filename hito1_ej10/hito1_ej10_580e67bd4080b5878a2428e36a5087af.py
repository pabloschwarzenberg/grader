usuario = ""
contraseña = ""
saldo_inicial = 1000000
cuenta = 100000

def pedirNumeroEntero():
    correcto=False
    num=""
    while(not correcto):
            num = input("Introduce N para ingresar al cajero automatico, introduce otra letra para salir\n")
            correcto=True
        
     
    return num

salir = False
opcion = 0
intentos = 0
while not salir:

    opcion = pedirNumeroEntero()

    if opcion == "N":
        usuario = input("Ingrese su usuario\n")
        contraseña = input("Ingrese la contraseña\n")

        if(usuario == "10334151" and contraseña == "1803"):
            while intentos < 3:
                print("Retirar dinero")
                contraseña = input("Ingrese la contraseña\n")
                intentos = intentos + 1
                
                if(contraseña == "1803"):
                    intentos = 0
                    monto = int(input("Ingrese el monto a retirar\n"))
                    if(monto <= cuenta and monto <= saldo_inicial):
                        cuenta = cuenta - monto
                        saldo_inicial = saldo_inicial - monto
                        break
                    else:
                        print("Monto no permitido")
                elif(intentos == 3):
                    print("Tarjeta Bloqueada")
                    break
                else:
                    print("Clave Invalida")
                    
        else:
            print("Usuario o contraseña invalidos")
    print("saldo cuenta=",cuenta, "saldo cajero=",saldo_inicial)
    if opcion != "N":
        salir = True