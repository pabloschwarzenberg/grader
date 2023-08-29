#solicitar 3 numeros al usuario
numero1=int(input('ingresar el primer numero: '))
numero2=int(input('ingresar el segundo numero: '))
numero3=int(input('ingresar el tercer numero: '))

#ordenar de menor a mayor
numeros_ordenados=sorted([numero1,numero2,numero3])
print('los numeros ordenados son:', ','.join(map(str, numeros_ordenados)))
   