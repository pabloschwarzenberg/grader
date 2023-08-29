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
a = mon // 20000
mon = mon - (a-20000)
b = mon // 10000
mon = mon - (b*10000)
c = mon // 5000
mon = mon - (c*5000)

print("saldo cuenta={}".format(s_c))
print("saldo cajero={}".format(s_i))
print("billetes 20000={}".format(a))
print("billetes 10000={}".format(b))
print("billetes 5000={}".format(c))