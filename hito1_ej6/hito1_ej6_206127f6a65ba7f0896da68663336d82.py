#Ordenar tres números
n1 = int(input('Ingrese numero 1 : '))
n2 = int(input('Ingrese numero 2 : '))
n3 = int(input('Ingrese numero 3 : '))

a = min(n1,n2,n3)
b = max(n1,n2,n3)
c = (n1 + n2 + n3) - a - b

print(a,',',c,',',b)