#Suma de los N primeros números
def suma_numeros(N):
suma=(numeroN*)(numeroN+1)//2 
return suma
numeroN=int(input("ingrese el valor de n: "))
resultado=suma_numeros(numeroN)
print("la suma de los primeros {}numeros naturales es:{}".format(numeroN,resultado))