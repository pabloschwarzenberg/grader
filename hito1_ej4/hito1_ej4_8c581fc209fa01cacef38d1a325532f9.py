#Conversión de Decimal a Binario
numero=int(input("ingrese un numero decimal positivo"))
binario= ""
if (numero>0):
  while(numero>0):
    if (numero%2==0):
       binario="0"+binario
    else:
       binario="1"+binario
    numero=int(match.floor(numero/2))
else:
  if (numero==0):
     binario="0"
  else:
    binario=("ingrese solo numero positivo: ")
print("la conversion da: "+binario)