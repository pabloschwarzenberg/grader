#Ordenar tres números
x=int(input("ponga en 1° numero: "))
y=int(input("ponga el 2° numero: "))
z=int(input("ponga el 3° numero: "))
if x<y and x<z:
    if y<z:
        print(str(x)+","+str(y)+","+str(z))
    else:
        print(str(x)+","+str(z)+","+str(y))
elif y<x and y<z:
    if x<z:
        print(str(y)+","+str(x)+","+str(z))
    else:
        print(str(y)+","+str(z)+","+str(x))
else:
    if x<y:
        print(str(z)+","+str(x)+","+str(y))
    else:
        print(str(z)+","+str(y)+","+str(x))
        
       