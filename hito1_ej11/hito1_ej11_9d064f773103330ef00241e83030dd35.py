#Cajero Automático
cajero = 1000000
usuario = [10334151, 1803, 100000]
a = int(input("Ingrese usuario: "))
b = int(input("Ingrese clave: "))
usua = [a, b]
count = 1
lista = [0, 0]
bill_20 = 20
bill_10 = 40
bill_5 = 40

while usua[1] != usuario[1] and count < 3:
    print("Clave invalida")
    b = int(input("Ingrese clave: "))
    count = count + 1
    if count == 3 and b != usuario[1]:
        print("Tarjeta bloqueada")
        break

while usua[1] == usuario[1] and usuario[2] > 0:
    c = input("Ingrese monto a retirar (Y para salir): ")

    if c.upper() == "Y":
        break

    if int(c) > usuario[2]:
        print("Monto no permitido")
    else:
        m = usuario[2] - int(c)
        usuario[2] = m
        cajero = cajero - int(c)
        t = str(usuario[2])
        u = str(cajero)
        lista[0] = "Saldo cuenta = " + t
        lista[1] = "Saldo cajero = " + u
        print(lista)

        # Distribución de billetes
        monto_restante = int(c)
        billetes_20000 = min(monto_restante // 20000, bill_20)
        monto_restante -= billetes_20000 * 20000
        bill_20 -= billetes_20000

        billetes_10000 = min(monto_restante // 10000, bill_10)
        monto_restante -= billetes_10000 * 10000
        bill_10 -= billetes_10000

        billetes_5000 = min(monto_restante // 5000, bill_5)
        monto_restante -= billetes_5000 * 5000
        bill_5 -= billetes_5000

        print("Billetes 20000 =", billetes_20000)
        print("Billetes 10000 =", billetes_10000)
        print("Billetes 5000 =", billetes_5000)      