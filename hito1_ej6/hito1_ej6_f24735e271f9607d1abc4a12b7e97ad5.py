#Ordenar tres números
n1 = int(input("Ingresa primer numero:"))
n2 = int(input("Ingresa segundo numero:"))
n3 = int(input("Ingresa tercer numero:"))
menor = min(n1,n2,n3)
mayor = max(n1,n2,n3)
medio = n1 +n2+n3 - menor - mayor
print(menor,",",medio,",",mayor)