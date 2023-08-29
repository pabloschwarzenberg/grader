#cajero
#variables de base.
usuario_base = "10334151"
clave_base = "1803"
intentos_login = 1

#saldo
saldo_cuenta = 100000 #100mil
saldo_cajero = 1000000 #1million

while intentos_login <= 4:
    print("para salir del cajero escribir exit.")
    clave_ingresada = input("ingresa tu clave: ")

    if clave_ingresada == clave_base:
        print("clave correcta")
        # mostrar datos.
        print(f"bienvenido usuario: {usuario_base}")
        print(f"el saldo disponible en la cuenta es: ${saldo_cuenta}")
        print(f"el saldo disponible en el cajero es: ${saldo_cajero}")

        #saldo a retirar
        saldo_retirar = input("ingrese el saldo a retirar: ")
        saldo_retirar = int(saldo_retirar)

        #reseteo de intentos.
        intentos = 1

        if saldo_retirar <= saldo_cuenta:
            print("monto permitido")
            
            #valores. 
            saldo_cuenta = saldo_cuenta - saldo_retirar
            saldo_cajero = saldo_cajero - saldo_retirar

            print(f"su monto final en cuenta es: {saldo_cuenta}")
            print(f"el monto final en el cajero es: {saldo_cajero}") 
        elif saldo_retirar > saldo_cuenta:
            print("monto no permitido")
    elif clave_ingresada == "exit":
        print("saliendo del cajero...")
        exit()

    else:
        print("clave invalida")

    if intentos_login == 3:
        print("tarjeta bloqueada")
        exit()
    elif intentos_login <= 3:
        intentos_login = intentos_login + 1
