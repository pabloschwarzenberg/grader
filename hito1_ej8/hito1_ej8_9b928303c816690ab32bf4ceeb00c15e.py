#Descomponer un número
X = str(input("Ingrese número de hasta 4 cifras: "))

A = int(X)

if 0< A <10:
    print(str(X),"U")
elif 10 < A <100:
    b = (X[0])
    c = (X[1])
    print(str(b),"D +", str(c),"U")
elif 100< A <1000:
    d = (X[0])
    e = (X[1])
    f = (X[2])
    print(str(d),"C +",str(e),"D +",str(f),"U")
elif 1000< A < 10000:
    g = (X[0])
    h = (X[1])
    j = (X[2])
    k = (X[3])
    print(str(g),"M +", str(h),"C +", str(j),"D +", str(k),"U")
else:
    print("Número no valido")
