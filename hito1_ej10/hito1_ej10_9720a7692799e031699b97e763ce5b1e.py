#Cajero Automático
cajero = 1000000
cuenta = 100000
usuario = "10334151"
contraseña = "1803"
n_cuenta = input("Ingrese su N° de cuenta: ")
if usuario == n_cuenta:
    contador = 0
    while contador < 3:
        clave = input("Ingrese su clave: ")
        if clave != contraseña:
            contador += 1
            print("clave invalida")
            if contador == 3:
                print("tarjeta bloqueada")
                break
            continue

        retiro = eval(input("cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
            suma = 1
            print(suma)
            saldo_cajero = cajero - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta)
            print("saldo cajero=", saldo_cajero)
            N = input()
            if N != "N":
                break
            else:
                continue