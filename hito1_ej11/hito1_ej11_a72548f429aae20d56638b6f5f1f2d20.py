#Cajero Automático
cajero = 1000000
cantBilletes20 = 20
cantBilletes10 = 40
cantBilletes5 = 40
billete5 = 5000
cuenta = 100000
admi = "10334151"
cl = "1803"
user = input("user: ")
if user == admi:
    contador = 0
    while contador < 3:
        clave = input("clave: ")
        if clave != cl:
            contador += 1
            print("Clave invalida")
            continue
        retiro = eval(input("¿Cuanto dinero desea retirar?"))
        if retiro > 100000:
            print("Monto no permitido")
        else:
            sumador = 1
            while True:
                if billete5 * sumador == retiro:
                    break
                sumador += 1
            print(sumador)
            saldoCajero = cajero - retiro
            saldoCuenta = cuenta - retiro
            print("Saldo cuenta =", saldo_cuenta, "\nSaldo cajero = ", saldoCajero, "\nbilletes 20000 = ", 0, "\nbilletes 10000 = ", 0, "\nbilletes 5000 = ", sumador)
            n = input()
            if n != "N":
                break
            else:
                continue
                continue