#Ordenar tres números
n1 = int(input("ingrese n 1: "))
n2 = int(input("ingrese n 2: "))
n3 = int(input("ingrese n 3: "))
menor = n1
mayor = n1
if menor > n2:
    menor = n2
if mayor < n2:
    mayor = n2
if menor > n3:
    menor = n3
if mayor < n3:
    mayor = n3
total = n1+n2+n3
x = total - mayor - menor
print(menor,x,mayor,sep=', ')  