#Ordenar tres números

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
m = max(n1,n2,n3)
n = min(n1,n2,n3)
r = (n1 + n2 + n3) - m - n
print (n, " , " , r , ", ", m)
  
  