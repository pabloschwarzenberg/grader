print("Ingrese Número de 4 Cifras:")

num = int(input())
mil = (num - (num % 1000)) / 1000
res = num % 1000
cen = (res - (res % 100)) / 100
res = num % 100
dec = (res - (res % 10)) / 10
uni = res % 10
MIL = "M"
CEN = "C"
DEC = "D"
UNI = "U"
m = int(mil)
c = int(cen)
d = int(dec)
u = int(uni)

print((m), str(MIL), "+", (c), str(CEN), "+", (d), str(DEC), "+", (u), str(UNI))
