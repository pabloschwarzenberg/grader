x = int(input("Ingrese un numero de hasta 4 digitos: "))
x = str(x)

if len(x) == 1:
    x = int(x)
    print(x,"U")
if len(x) == 2:
    u = x[1]
    u = int(u)
    d = x[0]
    d = int(d)
    print(d,"D + ",u,"U")
if len(x) == 3:
    c = x[0]
    c = int(c)
    d = x[1]
    d = int(d)
    u = x[2]
    u = int(u)
    print(c,"C + ",d,"D + ",u,"U")
if len(x) == 4:
    m = x[0]
    m = int(m)
    c = x[1]
    c = int(c)
    d = x[2]
    d = int(d)
    u = x[3]
    u = int(u)
    print(m,"M + ",c,"C + ",d,"D + ",u,"U")
      