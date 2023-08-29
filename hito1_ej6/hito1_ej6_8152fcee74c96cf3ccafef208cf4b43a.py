#Ordenar tres números
a = int(input("escriba el primer numero: "))
b = int(input("escriba el segundo numero: "))
c = int(input("escriba el tercer numero: "))
a1 = min(a,b,c)
b1 = max(a,b,c)
c1 = (a+b+c)-a1-b1
print("los numeros son", (a1,c1,b1))
