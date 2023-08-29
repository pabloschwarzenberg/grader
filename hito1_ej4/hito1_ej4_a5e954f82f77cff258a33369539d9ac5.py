#Conversión de Decimal a Binario
n=eval(input('Ingresar decimal: '))
lista=[]
i=1
while n>=1:
  lista.append(n%2)
  n=n//2
res=lista[::-1]
#while i<=len(lista):
#  print(lista[-i])
#  i=i+1
final=("".join(map(str, res)))
final=eval(final)
print('resultado= ',final)