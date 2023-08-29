#Ordenar tres números
a = int(input("Escriba el primer numero"))
b = int(input("Escriba el segundo numero"))
c = int(input("Escriba el tercer numero"))

d = min(a,b,c)
e = max(a,b,c)
f = (a + b + c ) -d - c

print("Acontinuyacion los numero ordenados de menor a mayor: {},{},{}" .format(d,f,e))