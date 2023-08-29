#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]  
    numeros.sort()  

    for i in range(len(numeros)):
        if i != len(numeros) - 1:
            print(numeros[i], end=", ")
        else:
            print(numeros[i])

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(numero1, numero2, numero3)
      