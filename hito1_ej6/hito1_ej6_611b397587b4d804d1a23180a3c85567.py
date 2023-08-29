#Ordenar tres números
x=[]
for i in range(0,3):
  numero=int(input("ingrese un número: "))
  x.append(numero)
x.sort()
print(x)