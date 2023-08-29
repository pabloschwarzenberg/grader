#Ordenar tres números
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))

numero_menor = min(num1,num2,num3)
numero_mayor = max(num1,num2,num3)
numero_central = (num1 + num2 + num3) - (numero_mayor + numero_menor)

print(str(numero_menor)+ "," + str(numero_central) + "," + str(numero_mayor))