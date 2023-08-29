#Ordenar tres números
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

v= min(n1,n2,n3)
v2= max(n1,n2,n3)
v3= (n1+n2+n3)-v-v2

print("El orden de menor a mayor es:{},{},{}". format(v, v3 ,v2))