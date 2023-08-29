#Ordenar tres números
#Ordenar tres numeros
n1= int(input("ingrese el primer numero:"))
n2= int(input("ingrese el segudo numero:"))
n3= int(input("ingrese el tercer numero:"))

a= min(n1, n2, n3)
c= max(n1, n2 , n3)
b=(n1 + n2 + n3) - a - c
print("Los numeros ordenados son:{}, {}, {}".format(a, b, c))      