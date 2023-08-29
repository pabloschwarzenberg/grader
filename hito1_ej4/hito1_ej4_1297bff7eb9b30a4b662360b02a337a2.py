#Conversión de Decimal a Binario
decimal= float(input("Ingrese un numero decimal: "))

if decimal<=0:
  decimal="0"
bin_=""
while decimal>0:
  resto=int(decimal%2)
  decimal=int(decimal/2)
  bin_=str(resto)+bin_

print("resultado = ",bin_)      