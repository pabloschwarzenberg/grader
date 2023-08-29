#Conversión de Decimal a Binario

def binario(x):
  a = bin(int(x))
  return a

0b111000

m = int(input("Ingrese numero a convertir"))
n = binario(m)
print ("resultado=",(str(n)[2::]))