#Cajero Automático
cajero = 1000000
cantidad_billetes_20 = 20
cantidad_billetes_10 = 40
cantidad_billetes_5 = 40
billete_5 = 5000
cuenta = 100000
admi = "10334151"
cl = "1803"
user = input("user: ")
if user == admi:
    contador = 0
    while contador < 3 :
        clave = input("clave: ")
        if clave != cl :
            contador += 1
            print("clave invalida")
            continue
        retiro = eval(input("cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
            #cuenta de billetes
            sumador = 1
            while True:
                if billete_5 * sumador == retiro :
                    break
                sumador += 1
            print(sumador)
            saldo_cajero = cajero - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta, "\nsaldo cajero=", saldo_cajero, "\nbilletes 20000=", 0, "\nbilletes 10000=", 0, "\nbilletes 5000=", sumador) 
            n = input()
            if n != "N" :
                break
            else:
                continue 