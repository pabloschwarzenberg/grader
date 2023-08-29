#Ordenar tres números
n=[]

for i in range(3):
    n.append(int(input("Ingrese un numero")))

n.sort()

for x in n:
    if(x==n[2]):
        print(x)
    else:
        print(x,end=",")