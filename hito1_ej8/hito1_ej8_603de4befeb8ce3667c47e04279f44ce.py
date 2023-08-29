#Descomponer un número
x = int(input("Numero: "))


if x >= 1000:
    m = x // 1000
    c = (x // 100) %10
    d = (x // 10) %10
    u = (x // 1) %10
    a = str(m) + "M + "+str(c) + "C + "+str(d) + "D + "+str(u) + "U"
    print(a)

elif x < 1000 and x >=100:
    c = (x // 100) %10
    d = (x // 10) %10
    u = (x // 1) %10
    a = str(c) + "C + "+str(d) + "D + "+str(u) + "U"
    print(a)
    
elif x < 100 and x >=10:
    d = (x // 10) %10
    u = (x // 1) %10
    a = str(d) + "D + "+str(u) + "U"
    print(a)
    
elif x < 10:
    u = (x // 1) %10
    a = str(u) + "U"
    print(a)