#Ordenar tres números de menor a mayor
n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
n3=int(input("Numero 3: "))
if (n1<n2):
  if (n1<=n3):
    primero=n1
    if (n2<n3):
      segundo=n2
      tercero=n3
    else:
      segundo=n3
      tercero=n2
  else:
      primero=n3
      segundo=n2
      tercero=n1        
else:
  if (n2<=n3):
    primero=n2
    if (n1<n3):
      segundo=n1
      tercero=n3
    else:
      segundo=n3
      tercero=n1
  else:
      primero=n3
      segundo=n2
      tercero=n1
print(primero,",",segundo,",",tercero)