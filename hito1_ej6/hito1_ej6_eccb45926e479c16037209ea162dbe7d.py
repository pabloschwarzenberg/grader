#Ordenar tres números
print("Programa para ordenar numeros enteros de menor a mayor")

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un numero entero: "))
numero3 = int(input("Ingrese un numero entero: "))

if(numero1<numero2 and numero2<numero3):
    print(numero1,",",numero2,",",numero3)
elif(numero2<numero1 and numero1<numero3):
    print(numero2,",",numero1,",",numero3)
elif(numero3<numero1 and numero1<numero2):
    print(numero3,",",numero1,",",numero2)
elif(numero3<numero2 and numero2<numero1):
    print(numero3,",",numero2,",",numero1)
elif(numero1<numero3 and numero3<numero2):
    print(numero1,",",numero3,",",numero2)
elif(numero2<numero3 and numero3<numero1):
    print(numero2,",",numero3,",",numero1)
elif(numero1 == numero2 == numero3):
    print(numero1,",",numero2,",",numero3)
elif(numero1 == numero2 and numero3<numero1):
    print(numero3,",", numero2,",",numero1)
elif(numero3 == numero2 and numero1<numero2):
    print(numero1,",",numero2,",",numero3)
elif(numero1 == numero3 and numero2<numero1):
    print(numero2,",",numero1,",",numero3)
elif(numero1 == numero2 and numero1<numero3):
    print(numero1,",",numero2,",",numero3)