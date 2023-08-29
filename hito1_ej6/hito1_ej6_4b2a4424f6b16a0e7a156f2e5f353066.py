#Ordenar tres números
print('\nPrograma que ordena tres números enteros\n')
try:
 a = int(input('Primer Número: '))
 b = int(input('Segundo Número: '))
 c = int(input('Tercer Número: '))
 numeros = [a,b,c]
 numeros.sort()
 print(*numeros, sep = ', ')
except:
 print('\nSólo números enteros')
      
        