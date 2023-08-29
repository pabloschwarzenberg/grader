def suma_n_primeros_numeros(N):
    suma=N*(N + 1)//2
    return suma
N=int(input("Ingrese numero: "))
resultado= suma_n_primeros_numeros(N)
print (resultado)