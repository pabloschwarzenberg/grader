# Entradas
n_1 = int(input("Ingrese un numero: "))
n_2 = int(input("Ingrese un numero: "))
n_3 = int(input("Ingrese un numero: "))

# Procesamiento

if n_1 == n_2 and n_1 > n_3:
    print(n_3, n_1, n_2,sep=",")
elif n_1 == n_2 and n_1 < n_3:
    print(n_1, n_2, n_3,sep=",")
elif n_1 == n_3 > n_2:
    print(n_2, n_1, n_3,sep=",")
elif n_1 == n_3 and n_1 < n_2:
    print(n_1, n_3, n_2,sep=",")
elif n_2 == n_3 and n_2 > n_1:
    print(n_1, n_2, n_3,sep=",")
elif n_2 == n_3 and n_2 < n_1:
    print(n_2, n_3, n_1,sep=",")
elif n_1 < n_2 and n_2 < n_3:
    print(n_1, n_2, n_3,sep=",")
elif n_1 < n_2 and n_2 > n_3:
    print(n_1, n_3, n_2,sep=",")
elif n_1 > n_2 and n_2 < n_3:
    print(n_2, n_1, n_3,sep=",")
elif n_1 > n_2 and n_2 < n_3:
    print(n_2, n_3, n_1,sep=",")
elif n_1 > n_2 and n_2 > n_3:
    print(n_3, n_2, n_1,sep=",")
elif n_1 < n_2 and n_2 > n_3:
    print(n_3, n_1, n_2,sep=",")
