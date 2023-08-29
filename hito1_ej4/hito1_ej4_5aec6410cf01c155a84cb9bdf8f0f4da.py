#Conversión de Decimal a Binario
n = int(input())
lista = []
while n >= 1:
  lista.insert(0,n%2)
  n = n//2
r = "".join(str(i)for i in lista)
print ("resultado=",r)