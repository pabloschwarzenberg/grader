#Ordenar tres números
   
num1=int(input('ingresar  primer numero: '))
num2=int(input('ingresar  segundo numero: '))
num3=int(input('ingresar  tercer numero: '))

#orden de menor a menor 
numeros_ordenados=sorted([num1,num2,num3])
print('los numeros ordenados son:', ','.join(map(str, numeros_ordenados)))

