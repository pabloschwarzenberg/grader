#Suma de los N primeros números
def suma_N_numeros(N):
    suma=N+1
    resultado=N*suma
    resultado_1=int(resultado/2)
    return resultado_1
a=int(input("Ingrese un número:"))
print(suma_N_numeros(a))

