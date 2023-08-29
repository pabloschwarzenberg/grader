n1 = int(input("ingrese su primer valor:"))
n2 = int(input("ingrese su segundo valor:"))
n3 = int(input("ingrese su tercer valor:"))

a = min(n1,n2,n3)
c = max(n1,n2,n3)
b = (n1 + n2 + n3) - a - c

print(a, ',',b, ',', c)