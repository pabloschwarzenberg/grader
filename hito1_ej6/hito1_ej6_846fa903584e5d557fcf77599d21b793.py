#Ordenar tres números
X = int(input("ingrese su primer numero: ")) 
Y = int(input("ingrese su segundo numero: ")) 
Z = int(input("ingrese su tercer numero: ")) 
Ma = max(X,Y,Z)
Me= min(X,Y,Z)
Med = (X + Y + Z) - Ma - Me 
print(Me," , ", Med , " , ", Ma) 
      