#Suma de los N primeros números
      def suma_numeros_naturales(n):
    suma = 0
    for i in range(1, n+1):
        suma = suma + i
    print("La suma de los", n, "primeros números naturales es:", suma)

 numero_n = int(input("Ingrese un número entero positivo: "))

 suma_numeros_naturales(numero_n)