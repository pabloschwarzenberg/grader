rut = int(input("ingresa el rut: "))
dig1 = rut //10000000
rut = rut % 10000000
dig2 = rut //1000000
rut = rut % 1000000
dig3 = rut //100000
rut = rut % 100000
dig4 = rut //10000
rut = rut % 10000
dig5 = rut //1000
rut = rut % 1000
dig6 = rut //100
rut = rut % 100
dig7 = rut //10
rut = rut % 10
dig8 = rut //1
suma = int((dig8 * 2) + (dig7 * 3) + (dig6 * 4) + (dig5 * 5) + (dig4 * 6) + (dig3 * 7) + (dig2 * 2) + (dig1 * 3))
div = int(suma // 11)
form = int(suma - (11*div))
rest = int(11 - form)

if rest == 11:
    print("dv=0")
elif rest == 10:
    print("dv=k")
else:
    print("dv=",rest)