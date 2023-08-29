#Descomponer un número
n = (input("ingrese un numero de maximo 4 digitos: "))
ns = str(n)
if len(ns) == 1:
    print("{}U".format(int(n[0])))
elif len(ns) == 2:
    d = int(n[0])
    u = int(n[1])
    print("{}D + {}U".format(d, u))
if len(ns) == 3:
    c = int(n[0])
    d =int(n[1])
    u = int(n[2])
    print("{}C + {}D + {}U".format(c, d, u))
elif len(ns) == 4:
    m = int(n[0])
    c = int(n[1])
    d = int(n[2])
    u = int(n[3])
    print("{}M + {}C + {}D + {}U".format(m, c, d, u))          