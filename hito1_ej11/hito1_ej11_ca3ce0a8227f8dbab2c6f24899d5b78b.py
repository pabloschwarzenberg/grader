total_cajero = 1000000
total_cuenta = 100000
usuario = 10334151
clave = 1803
ingreso = input("ingrese usuario: ")
ver=ingreso.isdigit()
c=0
if ver == True:
    ingreso=int(ingreso)
    while ingreso == usuario:
        clv = int(input("ingrese clave: "))
        if clv == clave:
            monto=int(input("monto a retirar: "))
            billetes = [20000, 10000, 5000]
            resto = monto
            for billetes in billetes:
                b = resto // billetes
                if b > 0:
                    if b == 0:
                        print("billetes",billetes,"=",b)
                    else:
                        print("billetes",billetes,"=",b)
                    resto %= billetes
            print("saldo cuenta={}".format(total_cuenta - monto))
            print("saldo cajero={}".format(total_cajero - monto))
            break

        else:
            if c == 2:
                print("tarjeta bloqueada")
                break
            else:
                c = c+1
                print("clave invalida")