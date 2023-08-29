#Cajero Automático
cajero = 1000000
cantidad_billetes_20 = 20
cantidad_billetes_10 = 40
cantidad_billetes_5 = 40
billete_5 = 5000
cuenta = 100000
el_poderosoadmin = "10334151"
contraseña = "1803"
user = input("user: ")
if user == el_poderosoadmin:
    contador = 0
    while contador < 3 :
        conbinacion = input("clave: ")
        if conbinacion != contraseña :
            contador += 1
            print("contraseña invalida")
            continue
        retiro = eval(input("cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
            saldo_cajero = cajero - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta,)
            print( "\nsaldo cajero=", saldo_cajero)
            n = input()
            if n != "N" :
                break
            else:
                continue      