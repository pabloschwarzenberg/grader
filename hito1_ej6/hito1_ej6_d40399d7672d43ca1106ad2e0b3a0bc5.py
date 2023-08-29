#Ordenar tres números
#Entradas
n_1 = int(input("Ingrese el primer número:"))
n_2 = int(input("Ingrese el segundo número:"))
n_3 = int(input("Ingrese el tercer número:"))

#Procesos
#Comparación de variables
if n_1 <= n_2 <= n_3:
    print(n_1,",",n_2,",",n_3)

elif n_1 <= n_3 <= n_2:
    print(n_1,",",n_3,",",n_2)

elif n_2 <= n_1 <= n_3:
    print(n_2,",",n_1,",",n_3)

elif n_2 <= n_3 <= n_1:
    print(n_2,",",n_3,",",n_1)

elif n_3 <= n_1 <= n_2:
    print(n_3,",",n_1,",",n_2)

elif n_3 <= n_2 <= n_1:
    print(n_3,",",n_2,",",n_1)