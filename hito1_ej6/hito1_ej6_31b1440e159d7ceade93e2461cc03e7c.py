#Ordenar tres números
n1 = eval(input("Numero 1: "))
n2 = eval(input("Numero 2: "))
n3 = eval(input("Numero 3: "))

x = max(n1,n2,n3)
y = min(n1,n2,n3)
z = (n1+n2+n3)-x-y

print(y,",",z,",",x)