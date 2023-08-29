#Conversión de Decimal a Binario
x=float(input("ingrese su numero:"))
lista=[]
while x > 0:
  otro=int(x%2)
  lista.append(otro)
  x=(x-otro)/2
  binario=""
for w in lista[::-1]:
  binario=binario + str(w)
print("resultado="+str(binario))