#Suma de los N primeros números
print('Ingrese un número para que el programa calcule la sumatoria de sus numeros naturales')

n=int(input('Ingrese el número que desea calcular: '))

while not n>0 :
    n = int(input('Error, vuleva a ingresar el número que desea calcular: '))
    
suma =  n*(n + 1)/2
print('El resultado es: ',suma)