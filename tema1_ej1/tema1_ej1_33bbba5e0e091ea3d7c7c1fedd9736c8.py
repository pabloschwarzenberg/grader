#Suma de los N primeros números
#Entradas
n = int(input("Ingrese un número hasta el cual sumar: "))

#Procedimiento
if n < 0:
    print ("Número invalido, por favor ingrese un numero natural")
    n = int(input("Ingrese un número hasta el cual sumar: "))
Sumatoria = int((n * (n+1))/2)

#Salidas

print ("La suma de los",n,"primeros números naturales es: ",Sumatoria)      