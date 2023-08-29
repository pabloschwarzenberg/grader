#Suma de los N primeros números
     numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es válido. Debe ser un número entero positivo.")
else:
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    print("La suma de los", numero, "primeros números naturales es:", suma)
  

