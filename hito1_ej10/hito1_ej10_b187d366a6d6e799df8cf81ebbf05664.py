cajero = 1000000
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
            saldo_cajero = cajero - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta, "saldo cajero=", saldo_cajero) 
            
            n = input()
            if n != "N" :
                break
            else:
                continue