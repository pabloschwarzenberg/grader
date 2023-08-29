#Ordenar tres números
numero1=int(input("Numero 1: "))
numero2=int(input("Numero 2: "))
numero3=int(input("Numero 3: "))
if (numero1<numero2):
  if (numero1<=numero3):
    primero=numero1
    if (numero2<numero3):
      segundo=numero2
      tercero=numero3
    else:
      segundo=numero3
      tercero=numero2
  else:
      primero=numero3
      segundo=numero2
      tercero=numero1        
else:
  if (numero2<=numero3):
    primero=numero2
    if (numero1<numero3):
      segundo=numero1
      tercero=numero3
    else:
      segundo=numero3
      tercero=numero1
  else:
      primero=numero3
      segundo=numero2
      tercero=numero1
print(primero,",",segundo,",",tercero)