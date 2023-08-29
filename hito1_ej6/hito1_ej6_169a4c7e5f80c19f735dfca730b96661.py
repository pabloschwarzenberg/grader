#declarar variables
A = int(input("ingrese primer numero: "))
B = int(input("ingrese segundo numero: "))
C = int(input("ingrese tercer numero: "))
#desarrollo    
X = min(A,B,C)
Z = max(A,B,C)
Y = (A+B+C)-X-Z
print("los numeros ordenados son {},{},{}".format(X,Y,Z))