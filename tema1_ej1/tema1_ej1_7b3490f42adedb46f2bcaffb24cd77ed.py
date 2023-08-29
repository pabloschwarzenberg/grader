def suma_naturales(n):
  suma = n*(n + 1)/2
  return suma 
  
numero = int(input('Ingrese un  Numero N:'))

suma_total = suma_naturales(numero)
print('La suma de los', numero, 'primeros números naturales es:', suma_total)