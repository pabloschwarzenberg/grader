#Conversión de Decimal a Binario
#Tomas Figueroa
def Binario(dec):
  binario = ""
  while dec//2 !=0:
    binario=str(dec%2)+binario
    dec=dec//2
  return str(dec)+binario
numero = int(input("inserte un numero: "))
print ("resultado=",Binario(numero))