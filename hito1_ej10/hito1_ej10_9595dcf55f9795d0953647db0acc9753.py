#Cajero Automático
cajero = 1000000
saldo = 100000
intentos = 3
print("Saldo de cajero es: ",cajero)
R = input("¿Desea realizar alguna operación en el cajero? s/n: ")
while R != "N":
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")
    if usuario == "10334151":
        if clave == "1803":
            print("Usted tiene $",saldo," en su cuenta.")
            monto = int(input("Ingrese monto a retirar: "))
            if monto <= cajero and monto <= saldo:
                    saldo = saldo - monto
                    cajero = cajero - monto
                    print("saldo cuenta=",saldo)
                    print("saldo cajero=",cajero)
            else:
                    print("monto no permitido")
        else:
            print("clave invalida")
            while intentos != 0:
                intentos = intentos - 1
                clave = input("Ingrese clave nuevamente: ")
            if intentos == 0:
                print("tarjeta bloqueada")
                break
    else:
        pass   
    R = input("¿Desea realizar otra operación en el cajero? s/n: ") 