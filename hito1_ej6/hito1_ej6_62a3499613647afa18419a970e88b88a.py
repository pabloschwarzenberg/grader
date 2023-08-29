n = int(input("ingrese el primer numero aleatorio: "))
m = int(input("ingrese el segundo numero aleatorio: "))
o = int(input("ingrese el tercer numero aleatorio: "))

a = min(n, m, o)
c = max(n, m, o)
b = (n + m + o) - a - c

print(a,",",b,",",c)