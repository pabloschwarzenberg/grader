#Ordenar tres números
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

l = [n1,n2,n3]

l.sort()
print("los numeros ordenados de menor a mayor son: ", l[0], ",", l[1], ",", l[2])
