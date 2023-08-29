#Descomponer un número
n = int(input("ingresa un numero:"))

if (0 < n < 10):
    p = str(n)
    u = p[0]
    print(u,"U")
elif (9 < n < 100):
    p = str(n)
    u = p[1]
    d = p[0]
    print(d,"D + ",u,"U")
elif (99 < n < 1000):
    p = str(n)
    u =p[2]
    d =p[1]
    c =p[0]
    print(c,"C + ",d,"D + ",u,"U")
    
elif (999 < n < 10000):
    p = str(n)
    u =p[3:4]
    d =p[2:3]
    c =p[1:2]
    m =p[0:1]
    print(m,"M +",c,"C + ",d,"D + ",u,"U")     