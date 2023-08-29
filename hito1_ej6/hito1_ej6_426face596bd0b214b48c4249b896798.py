#Ordenar tres números
uno = int(input("Ingresa el primer numero: "))
dos = int(input("Ingresa el segundo numero: "))
tres = int(input("Ingresa el tercer numero: "))

if uno < dos and uno < tres:
  primero = uno
  if dos < tres:
    segundo = dos
    tercero = tres
  else:
    segundo = tres
    tercero = dos

elif dos < uno and dos < tres:
  primero = dos
  if uno < tres:
    segundo = uno
    tercero = tres
  else:
     segundo = tres
     tercero = uno
else:
  primero = tres
  if dos < uno:
    segundo = dos
    tercero = uno
  else:
    segundo = uno
    tercero = dos
    
print(primero,",",segundo,",",tercero)
 
    