#Ordenar tres números
numeroA= eval(input("ingrese un numero: "))
numeroB= eval(input("ingrese un segundo numero: "))
numeroC= eval(input("ingrese un tercer numero: "))
numeros= numeroA, numeroB, numeroC
orden= sorted(numeros)
print(orden)