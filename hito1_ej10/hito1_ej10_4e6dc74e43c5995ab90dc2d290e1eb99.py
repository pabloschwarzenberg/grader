# Cajero automatico.

# datos cajero and usuario.
clave = "1803"
usuario = "10334151"
saldo_usuario = 100000
saldo_cajero = 1000000

while True:

    #variables de ciclos.
    intentos = 1

    #bienvenida.
    print("~"*30)
    print("Bienvenido Usuario: " + usuario)
    print("para salir escribir exit")
    print("~"*30)

    #Ingreso
    while True:    
            clave_i = input("Ingrese su clave: ")
            print("~"*30)
            if clave_i == clave:
                print("Clave correcta.")
                print("~"*30)
                break
            elif clave_i == "exit":
                exit()
            elif intentos == 3:
                print("Maximos de intentos permitidos.")
                print("Tarjeta bloqueada.")
                print("~"*30)
                exit()
            else:
                print("Clave invalida.")
                print("Intentelo de nuevo")
                print("~"*30)
                intentos = intentos + 1

    #Sacar money
    while True:
        dinero = input("Monto a retirar: ")
        print("~"*30)
        try:
            dinero = int(dinero)
            if 0 <= dinero <= 100000:
                if saldo_usuario > 0:
                    saldo_usuario = saldo_usuario - dinero
                    print("Saldo cuenta =", saldo_usuario)
                    saldo_cajero = saldo_cajero - dinero
                    print("Saldo cajero =", saldo_cajero)
                    break
                else:
                    print("No tiene saldo Suficiente.")
                    print("~"*30)
                    exit()
            else:
                print("Monto no valido.")
                print("~"*30)
        except ValueError or SyntaxError:
            print("Error.")
            print("~"*30)
