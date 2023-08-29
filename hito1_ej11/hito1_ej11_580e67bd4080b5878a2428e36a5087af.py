usuario = ""
contraseña = ""
saldo_inicial = 1000000
cuenta = 100000

billete20000 = [20000]
billete10000 = [10000]
billete5000  = [5000]

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
                            i = 0
                            a = 0
                            b = 0
                            c = 0
                            
                            a += int(monto / billete20000[i])
                            monto = int(monto % billete20000[i])

                            b += int(monto / billete10000[i])
                            monto = int(monto % billete10000[i])

                            c += int(monto / billete5000[i])
                            monto = int(monto % billete5000[i])
                            
                            print("Billetes de 20000: ", a)
                            print("Billetes de 10000: ", b)
                            print("Billetes de 5000: ", c)
                            cuenta = cuenta - (monto + (a*20000) + (b*10000) + (c*5000))
                            saldo_inicial = saldo_inicial - (monto + (a*20000) + (b*10000) + (c*5000))
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
    print("Estado de la cuenta: ",cuenta, "Saldo Inicial: ", saldo_inicial)
    if opcion != "N":
        salir = True