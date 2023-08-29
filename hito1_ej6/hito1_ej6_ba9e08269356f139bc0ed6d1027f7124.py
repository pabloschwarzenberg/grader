#Ordenar tres números
#Ordenar tres números
n1=int(input("numero1:"))
n2=int(input("numero2:"))
n3=int(input("numero3:"))
mayor,medio,menor=0,0,0

if n1>n2 and n1>n3:
    mayor=n1
    if n2>n3:
        medio,menor=n2,n3
    else:
        medio,menor=n3,n2
elif n2>n1 and n2>n3:
    mayor=n2
    if n1>n3:
        medio,menor=n2,n3
    else:
        medio,menor=n3,n2
else:
    mayor=n3
    if n1>=n2:
        medio,menor=n1,n2
    else:
        medio,menor=n2,n1
    
print(menor,",",medio,",",mayor)
