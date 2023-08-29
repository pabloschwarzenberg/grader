#Ordenar tres números
Z=int(input("ingrese numero 1  : "))
Y=int(input("ingrese numero 2  : "))
X=int(input("ingrese numero 3  : "))
if(Z<=Y<=X):
  print(str(Z)+","+str(Y)+","+str(X))
elif(Z<=X<=Y):
  print(str(Z)+","+str(X)+","+str(Y))
elif(Y<=Z<=X):
  print(str(Y)+","+str(Z)+","+str(X))
elif(Y<=X<=Z):
  print(str(Y)+","+str(X)+","+str(Z))
elif(X<=Z<=Y):
  print(str(X)+","+str(Z)+","+str(Y))
elif(X<=Y<=Z):
  print(str(X)+","+str(Y)+","+str(Z))     