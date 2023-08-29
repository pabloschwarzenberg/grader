s_i = 1000000
s_c  = 100000
i = 0
u = int(input())
while(i < 3 or c == "N"):
    c   = str(input("Clave: "))
    if c != "1803" or u != 10334151:
        print("clave invalida o usuario invalido.")
        i = i + 1
    elif c == "1803":
        mon = int(input("Monto a retirar: "))
        if mon > 100000 or mon <= 0:
            print("monto no permitido o invalido.")
        else:
            s_i = s_i - mon
            s_c = s_c - mon
        break
print("saldo cuenta={}".format(s_c))
print("saldo cajero={}".format(s_i))