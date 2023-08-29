#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n*(n+1))//2
    return suma
#solicitar el numero al usario
n=int(input('ingrese un numero n: '))
#suma de los n numeros naturales 
resultado = suma_numeros_naturales(n)
print('la suma de los primeros', n,'numeros naturales es', resultado)
