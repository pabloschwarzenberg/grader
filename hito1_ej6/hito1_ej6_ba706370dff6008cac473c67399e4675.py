num_1 = int(input("Escriba el primer numero: "))
num_2 = int(input("Escriba el segundo numero: "))    
num_3 = int(input("Escriba el tercer numero: "))    

menor = num_1
medio = num_2
mayor = num_3

if num_2 < menor:
    menor = num_2
    medio = num_1
    mayor = num_3

if num_3 < menor:
    menor = num_3
    medio = num_1 if num_1 < num_2 else num_2
    mayor = num_1 if num_1 > num_2 else num_2
elif num_3 < medio:
    medio = num_3
    mayor = num_2 if num_2 > num_1 else num_1

numeros_ordenados = f"{menor},{medio},{mayor}"
print("Números ordenados:", numeros_ordenados)
