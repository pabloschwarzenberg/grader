#Descomponer un número

#Entradas

n = int(input("Ingrese un número de hasta 4 dígitos: "))

#Procesamiento

if n <= 9999:
    M = n // 1000
    res = n - (M * 1000)
    C = res // 100
    res = res - (C * 100)
    D = res // 10
    U = res - (D * 10)

#Salida

print(str(M) + "M +" + str(C) + "C +" + str(D) + "D +" + str(U) + "U")