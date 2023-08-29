#Ordenar tres números
num1 = int(input('Ingrese un numero'))
num2 = int(input('Ingrese otro numero'))
num3 = int(input('Ingrese nuevamente un numero'))
num4 = [num1, num3, num2]
secuencia = sorted(num4)
print(*(secuencia), sep=',')