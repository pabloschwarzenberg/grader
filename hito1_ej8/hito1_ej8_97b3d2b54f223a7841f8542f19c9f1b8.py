#Descomponer un número
numero=int(input("ingresar numero: "))
x=str(numero)
if len(x)==1:
    m = x[0]
    print(m, "U")

if len(x) == 2:
    d = x[0]
    u = x[1]
    print(d,"D +",u,"U" )

if len(x) == 3:
    c = x[0]
    d = x[1]
    u = x[2]
    print(c, "C +", d, "D +",u,"U")
if len(x) == 4:
    m = x[0]
    c = x[1]
    d = x[2]
    u = x[3]
    print(m,"M +", c, "C +", d, "D +", u, "U")     