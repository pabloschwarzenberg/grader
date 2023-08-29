#Ordenar tres números
def orden_numeros(num1,num2,num3):
    numeros = [num1,num2,num3]
    numeros.sort()
    print(",".join(str(num) for num in numeros))
numero1 = int(input("Ingrese le primero numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero:  "))

orden_numeros(numero1,numero2,numero3)
    