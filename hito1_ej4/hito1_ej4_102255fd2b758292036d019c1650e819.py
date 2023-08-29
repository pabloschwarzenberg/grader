#Conversión de Decimal a Binario
def fbinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(" resultado="+ str(fbinario(numero)))

#Números Primos
#Escribe una función llamada es_primo que retorne True cuando un número es primo y False cuando no lo es.
def es_primo(num):
 if num < 2:     
  return False
 for i in range(2, num): 
  if num % i == 0:  
   return False
 return True