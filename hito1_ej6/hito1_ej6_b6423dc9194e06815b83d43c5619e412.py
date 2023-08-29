#Ordenar tres números
X=input("Ingrese primer numero")
Y=input("Ingrese segundo numero")
Z=input("Ingrese tercer numero")
if(X<=Y<=Z):
  print(X,",",Y,",",Z)
if(X>=Y<=Z):
  print(Y,",",X,",",Z)
if(X>=Y>=Z):
  print(Z,",",Y,",",X)
if(X>=Z>=Y):
  print(Y,",",Z,",",X)