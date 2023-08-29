#Conversión de Decimal a Binario
d=int(input("Introducir numero decimal: "))
t = ""
while d > 0:
    c = d % 2
    d = d // 2
    t = t + str(c)
p = len(t)
k = ""
while p > 0:
    k = k + t[p - 1]
    p -=1
print("resultado= "+str(k))    