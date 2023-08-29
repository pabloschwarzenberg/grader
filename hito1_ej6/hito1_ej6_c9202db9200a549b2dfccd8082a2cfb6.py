#Ordenar tres números
n = int(input("escriba un numero entero: "))
n2 = int(input("escriba un numero entero: "))
n3 = int(input("escriba un numero entero: "))

a = min(n, n2, n3)
b = max(n, n2, n3)
c = (n + n2 + n3) - a - b 

print(a,',',c,',',b)