#Conversión de Decimal a Binario
n= int(input("Ingrese número decimal: "))
lista = []
while n>0:
  r = int(n%2)
  lista.append(r)
  n = (n-r)/2
nb = ""
for e in lista[::-1]:
 nb = nb + str(e)

print("resultado="+str(nb))