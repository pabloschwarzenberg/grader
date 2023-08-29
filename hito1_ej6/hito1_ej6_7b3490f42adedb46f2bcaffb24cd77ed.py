def ordenar_numeros(num1, num2, num3):
   
  numeros = [num1, num2, num3]
  numeros.sort()
  return numeros

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero:' ))
numero3 = int(input('Ingrese el tercer numero: '))

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
resultado = ', '.join(str(num) for num in numeros_ordenados)
print('Numeros ordenados de menor a mayor:', resultado)