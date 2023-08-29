#Ordenar tres números
a = eval(input("Digite un número:"))
b = eval(input("Digite otro número:"))
c = eval(input("Digite el último número:"))

Menor = min(a,b,c)
Mayor = max(a,b,c)
Medio = (a + b + c) - Mayor - Menor

print("{},{},{}".format(Menor , Medio , Mayor))