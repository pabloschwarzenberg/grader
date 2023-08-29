#Suma de los N primeros números

print("****************************************")
print("*Suma de los primeros números naturales*")
print("****************************************")

#Solicitar valores.

n = float(input("Ingrese un número natural: "))
suma_num_naturales = float(n*(n+1)/2)
suma_num_naturales = round(suma_num_naturales,2)

#Planteamos el desarrollo de la sentencia.

if n > 0 and n < 1:
    print("El resultado de la suma es : ", suma_num_naturales)
elif n == 0:
    print("El resultado de la suma es : ", suma_num_naturales)
elif n >= 1:
    print("El resultado de la suma es: ", suma_num_naturales)
else:
    print("El número no es natural, intentelo nuevamente.")

#Termino del programa.
print("Fin.")      