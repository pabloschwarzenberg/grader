#Conversión de Decimal a Binario
def binario(numero):
  bin=""
  while numero // 2!=0:
    bin=str(numero%2)+bin
    numero=numero//2
  return str(numero)+bin

b=int(input("Ingrese un numero:"))
print("resultado=",binario(b))