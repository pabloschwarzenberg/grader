#Ordenar tres números
print("Ingrese tres numeros enteros para que se ordenen de menor a mayor.")

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

mayor = max(num_1,num_2,num_3)
menor = min(num_1,num_2,num_3)
medio = (num_1 + num_2 + num_3) - menor - mayor

print(menor,",",medio,",",mayor)