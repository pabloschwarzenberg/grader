#SUMA DE LOS N PRIMEROS NATURALES

#ENTRADA
numero = int(input('Ingrese un numero: '))

#PROCESAMIENTO
i = 0
suma = 0

while i <= numero : 
    suma = suma + i
    i = i+1 


#SALIDA
print('La suma de los primeros',numero,'numeros es: ',suma)
      