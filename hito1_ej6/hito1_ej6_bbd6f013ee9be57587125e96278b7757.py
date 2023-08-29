#Ordenar tres números
l =[None]*3
for i in range(len(l)):
  n = int(input("Ingrese un numero: "))
  l[i]=n
l.sort()
print("{},{},{}".format(l[0],l[1],l[2]))