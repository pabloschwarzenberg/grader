#Suma de los N primeros números
def sumatoria(Y,N):
  if (N>0):
    Y=sumatoria(Y,N-1)
    Y=Y+N
    return Y
  else:
    Y=0
    return Y
  
  
Y=0
N=int(input("ingrese\n"))
Y=sumatoria(Y,N)
print(Y)


