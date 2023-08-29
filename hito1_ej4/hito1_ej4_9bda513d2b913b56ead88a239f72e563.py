print("Conversir decimal a binario")
decimal=int(input("Introduzca un numero decimal:"))
binario=""
validador=True
while validador==True:
  binario=str(decimal%2)+binario
  decimal=decimal//2
  if decimal==0:
    validador=False
print("Resultado=",binario)

