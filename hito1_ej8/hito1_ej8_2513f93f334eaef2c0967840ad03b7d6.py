#Descomponer un número

n = int(input("Ingrese un número de hasta 4 dígitos: "))

if n < 10:
    u = str(n)
    print(u + "U")
elif n < 100:
    d = int(n/10)
    u = n - d*10
    print(str(d) + "D + " + str(u) + "U")
elif n < 1000:
    c = int(n/100)
    d = int(n/10) - c*10
    u = n - d*10 - c*100
    print(str(c) + "C + " + str(d) + "D + " + str(u) + "U")
elif n < 10000:
    m = int(n/1000)
    c = int(n/100) - m*10
    d = int(n/10) - c*10 - m*100
    u = n - d*10 - c*100 - m*1000
    print(str(m) + "M + " + str(c) + "C + " + str(d) + "D + " + str(u) + "U")