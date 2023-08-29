#Factores Primos
numero=int(input("ingrese un numero: "))
resto=numero
i=2
while i<numero:
  j=2
  es_primo=True
  while j<i:
    if i%j==0:
      es_primo=False
      break
    j=j+1
  if es_primo:
    while resto%i==0:
      print(i)
      resto=resto//i
  i=i+1
if resto==numero:
  print(resto)
     