#Conversión de Decimal a Binario
n=float(input())

def binarizar(n):
  binario= ''
  while decimal // 2!=0:
    binario = str(n % 2) + binario
    n= n//2
    n= str(n) + binario

print( "resultado= ",n)
