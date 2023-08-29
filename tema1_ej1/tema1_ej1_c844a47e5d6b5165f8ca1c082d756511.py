#Suma de los N primeros números
def sumatoria(X,N):
 if(N>0):
  X=sumatoria(X,N-1)
  X=X+N
  return X
 else:
  X=0
  return X
X=0
N=int(input("ingrese un numero\n"))
X=sumatoria(X,N)
print(X)