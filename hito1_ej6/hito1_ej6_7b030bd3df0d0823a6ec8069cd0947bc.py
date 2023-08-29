numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
numero3 = int(input("Ingrese tercer numero: "))

if(numero2 > numero1 < numero3):
    numero_menor = numero1
    if(numero2 < numero3):
        numero_intermedio = numero2
        numero_mayor = numero3
        print(numero_menor,",",numero_intermedio,",",numero_mayor)

    else:
        numero_intermedio = numero3
        numero_mayor = numero2
        print(numero_menor,",",numero_intermedio,",",numero_mayor)
      
if(numero1 > numero2 < numero3):
    numero_menor = numero2
    if(numero1 < numero3):
        numero_intermedio = numero1
        numero_mayor = numero3
        print(numero_menor,",",numero_intermedio,",",numero_mayor)

    else:
        numero_intermedio = numero3
        numero_mayor = numero1
        print(numero_menor,",",numero_intermedio,",",numero_mayor)

if(numero1 > numero3 < numero2):
    numero_menor = numero3
    if(numero1 < numero2):
        numero_intermedio = numero1
        numero_mayor = numero2
        print(numero_menor,",",numero_intermedio,",",numero_mayor)

    else:
        numero_intermedio = numero2
        numero_mayor = numero1
        print(numero_menor,",",numero_intermedio,",",numero_mayor)