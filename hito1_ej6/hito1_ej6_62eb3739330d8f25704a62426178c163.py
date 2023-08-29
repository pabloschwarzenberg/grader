#Ordenar tres números
A = int(input("ingrese primer numero: "))
B = int(input("ingrese segundo numero: "))
C = int(input("ingrese tercer numero: "))
#desarrollo
X = min(A,B,C)
m = max(A,B,C)
l = (A+B+C)-X-m
print("los numeros ordenados son {},{},{}".format(X,l,m))