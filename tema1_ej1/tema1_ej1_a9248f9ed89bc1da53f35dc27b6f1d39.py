#Suma de los N primeros números
N1=int(input("Introduzca su numero para ser el limite de la sumatoria: "))
n=0
N=0
while(N1>=n):
    n=n+1
    N=n+N
    if(N1==n):
        break
    else:
        continue
print("Su resultado es: "+str(N))