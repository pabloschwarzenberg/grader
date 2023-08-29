#Suma de los N primeros números
def suma_numeros_naturalez(n):
    suma  = n*(n+1)//2
    return  suma
N = int(input("Ingrese el valor de N: "))
resultado = suma_numeros_naturalez(N)
print("la suma de los",N,"primeros numeros naturales es:",resultado)