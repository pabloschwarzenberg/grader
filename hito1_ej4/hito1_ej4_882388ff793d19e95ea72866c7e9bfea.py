decimal=int(input("ingrese un numero"))
binario=""
while decimal>0:
  residuo=decimal%2
  decimal=decimal//2
  binario=str(residuo)+binario

print("resultado=",binario)