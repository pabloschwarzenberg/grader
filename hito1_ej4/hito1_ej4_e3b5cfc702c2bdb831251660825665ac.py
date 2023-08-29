#Conversión de Decimal a Binario
n = int(input())
d=[]
while(n>=1):
  d.append(n%2)
  n=int(n/2)

  S=d[::-1]
d = ''.join(map(str,S))
print("resultado="+d)