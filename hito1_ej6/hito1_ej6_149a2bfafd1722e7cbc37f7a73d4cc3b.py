#Ordenar tres números
#solicitar 3 numeros al usuario
num1=int(input('ingresar el primer numero: '))
num2=int(input('ingresar el segundo numero: '))
num3=int(input('ingresar el tercer numero: '))

#orden de menor a menor 
numeros_ordenados=sorted([num1,num2,num3])
print('los numeros ordenados son:', ','.join(map(str, numeros_ordenados)))
    