numero= int(input("es_primo: "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
if contador > 0 :
  print("False" )
else:
  print("True")
