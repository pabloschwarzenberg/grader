#Cajero Automático
  
cajero_A = 1000000
c_billetes_20 = 20
c_billetes_10 = 40
c_billetes_5 = 40
billete_5 = 5000
cuenta = 100000
ADMIN = "10334151"
password = "1803"
user = input("user: ")
if user == ADMIN:
    contador = 0
    while contador < 3 :
        contraseña = input("su contraseña: ")
        if contraseña != password :
            contador += 1
            print("conraseña incorrecta")
            continue
        retiro = eval(input("cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
        
            sumador = 1
            while True:
                if billete_5 * sumador == retiro :
                    break
                sumador += 1
            print(sumador)
            saldo_cajero = cajero_A - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta, "\nsaldo cajero=", saldo_cajero, "\nbilletes 20000=", 0, "\nbilletes 10000=", 0, "\nbilletes 5000=", sumador)
            n = input()
            if n != "N" :
                break
            else:
                continue