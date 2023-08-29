#Ordenar tres números
num1 = int(input('primer numero: '))
num2 = int(input('segundo numero: '))
num3 = int(input('tercer numero: '))
#la funcion min elige el valor minimo en un iterable
primer_lugar = min(num1, num2, num3)
#la funcion max elige el valor maximo en un iterable
tercer_lugar = max(num1, num2, num3)
#se suman los 3 numeros y se le restan el valor maximo y minimo para determinar el valor del medio.
segundo_lugar = num1 + num2 + num3 - primer_lugar - tercer_lugar
print(primer_lugar, end='')
print(',', end='')
print(segundo_lugar, end='')
print(',', end='')
print(tercer_lugar, end='')
